import subprocess
import threading
import time
import json
import paho.mqtt.client as mqtt
from sqlite_logger import log_gmdss_data, conn as db_conn, c as db_cursor # Import logging function and db connection

# MQTT Configuration
MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPIC = "gmdss/data"

# --- MQTT Callback functions ---
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[Coordinator/MQTT] Connected successfully to {MQTT_BROKER}.")
        client.subscribe(MQTT_TOPIC)
        print(f"[Coordinator/MQTT] Subscribed to topic: {MQTT_TOPIC}")
    else:
        print(f"[Coordinator/MQTT] Connection failed with code {rc}")

def on_message(client, userdata, msg):
    print(f"[Coordinator/MQTT] Received message on {msg.topic}: {msg.payload.decode()}")
    try:
        data = json.loads(msg.payload.decode())
        # TODO: Add any necessary data validation or transformation here
        log_gmdss_data(data) # Log data to SQLite
        print(f"[Coordinator/SQLite] Data logged: {data}")
    except json.JSONDecodeError:
        print("[Coordinator/MQTT] Error decoding JSON from message.")
    except Exception as e:
        print(f"[Coordinator/MQTT] Error processing message or logging data: {e}")

def setup_mqtt_client():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "GMDSS_Coordinator_Subscriber")
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(MQTT_BROKER)
        return client
    except Exception as e:
        print(f"[Coordinator/MQTT] Error connecting to MQTT broker: {e}")
        return None

def run_script(command, name):
    print(f"[Coordinator] Starting {name}...")
    try:
        # Using Popen for non-blocking execution if needed, or run for blocking.
        # For components like mqtt_telemetry, they run indefinitely, so Popen is better.
        process = subprocess.Popen(command, shell=True)
        print(f"[Coordinator] {name} started with PID {process.pid}.")
        return process
    except Exception as e:
        print(f"[Coordinator] Error running {name}: {e}")
        return None
    # No "finished" message here as these are long-running services

if __name__ == "__main__":
    # Initialize MQTT client for the coordinator
    mqtt_client = setup_mqtt_client()

    if not mqtt_client:
        print("[Coordinator] Exiting due to MQTT setup failure.")
        exit()

    # Start the MQTT client loop in a separate thread
    mqtt_thread = threading.Thread(target=mqtt_client.loop_forever)
    mqtt_thread.daemon = True # Allow main program to exit even if this thread is running
    mqtt_thread.start()
    print("[Coordinator] MQTT client loop started in a separate thread.")

    # Define components to run.
    # sqlite_logger.py is NOT run as a separate script anymore, as its functions are imported.
    # water_sensor.py might also publish to MQTT or be handled differently. For now, keep it.
    components_to_run = [
        ("python3 python/mqtt_telemetry.py", "MQTT GMDSS Publisher"), # This will publish data
        # ("python3 python/water_sensor.py", "Water Sensor"), # Assuming this is another data source
        # ("python3 python/rest_api.py", "REST API"), # May depend on the DB, start after coordinator setup
        # ("python3 python/interface_gui.py", "GUI")
    ]

    processes = []
    for cmd, name in components_to_run:
        proc = run_script(cmd, name)
        if proc:
            processes.append(proc)

    print("[Coordinator] System coordinator running. Will shut down automatically after ~20 seconds.")

    shutdown_time = time.time() + 20 # Run for 20 seconds

    try:
        # Keep the main thread alive to allow background threads (MQTT, subprocesses) to run
        while time.time() < shutdown_time:
            if not mqtt_thread.is_alive():
                print("[Coordinator] MQTT thread has stopped unexpectedly.")
                break
            # Check if telemetry process has ended
            if processes:
                publisher_proc = processes[0] # Assuming the first one is the publisher
                if publisher_proc.poll() is not None: # Process has terminated
                    print(f"[Coordinator] Monitored process {publisher_proc.pid} (MQTT GMDSS Publisher) has terminated.")
                    # Give a few more seconds for MQTT messages to be processed
                    time.sleep(5)
                    break
            time.sleep(1)
        print("[Coordinator] Programmed shutdown initiated.")
    except KeyboardInterrupt:
        print("[Coordinator] Manual shutdown initiated (Ctrl+C)...")
    finally:
        print("[Coordinator] Starting final shutdown sequence...")
        if mqtt_client:
            mqtt_client.disconnect()
            print("[Coordinator/MQTT] Disconnected.")

        for proc in processes:
            proc.terminate() # Terminate subprocesses
            proc.wait()
            print(f"[Coordinator] Terminated process {proc.pid}.")

        if db_conn: # Close the SQLite connection
            db_conn.close()
            print("[Coordinator/SQLite] Database connection closed.")

        print("[Coordinator] All systems shut down.")
