import subprocess
import threading

def run_script(command, name):
    print(f"[Coordinator] Starting {name}...")
    try:
        subprocess.call(command, shell=True)
    except Exception as e:
        print(f"[Coordinator] Error running {name}: {e}")
    print(f"[Coordinator] {name} finished.")

if __name__ == "__main__":
    components = [
        ("python3 python/water_sensor.py", "Water Sensor"),
        ("python3 python/mqtt_telemetry.py", "MQTT Telemetry"),
        ("python3 python/sqlite_logger.py", "SQLite Logger"),
        ("python3 python/rest_api.py", "REST API"),
        ("python3 python/interface_gui.py", "GUI")
    ]

    threads = []
    for cmd, name in components:
        thread = threading.Thread(target=run_script, args=(cmd, name))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("[Coordinator] All systems completed.")
