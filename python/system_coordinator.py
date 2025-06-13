import subprocess
import threading
import logging

# Configure basic logging for the coordinator
logging.basicConfig(level=logging.INFO, format='[Coordinator] %(levelname)s: %(message)s')

def run_script(command_parts, name):
    logging.info(f"Starting {name} ({' '.join(command_parts)})...")
    try:
        # Using shell=False is generally safer
        process = subprocess.run(command_parts, shell=False, capture_output=True, text=True, check=False)

        if process.stdout:
            logging.info(f"Output from {name}:\n{process.stdout}")

        if process.stderr:
            logging.error(f"Errors from {name}:\n{process.stderr}")

        if process.returncode != 0:
            if name == "System Diagnostics":
                logging.critical(f"System Diagnostics failed! Exit code: {process.returncode}")
            else:
                logging.warning(f"{name} exited with code {process.returncode}")
        else:
            logging.info(f"{name} completed successfully.")

    except FileNotFoundError:
        logging.error(f"Error running {name}: The command '{command_parts[0]}' was not found. Ensure it is installed and in PATH.")
    except PermissionError:
        logging.error(f"Error running {name}: Permission denied for command '{command_parts[0]}'. Check execute permissions.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while running {name} ({' '.join(command_parts)}): {e}")

    logging.info(f"{name} execution attempt finished.")

if __name__ == "__main__":
    # Assuming diag_proc is the compiled C++ diagnostics executable in the root directory
    # For C++ components, ensure they are compiled and executable.
    # Example: ["./diag_proc"] or ["build/diag_proc"] if it's in a subdirectory
    components = [
        (["./diag_proc"], "System Diagnostics"), # Added C++ diagnostics
        (["python3", "python/water_sensor.py"], "Water Sensor"),
        (["python3", "python/mqtt_telemetry.py"], "MQTT Telemetry"),
        (["python3", "python/sqlite_logger.py"], "SQLite Logger"),
        (["python3", "python/rest_api.py"], "REST API"),
        (["python3", "python/interface_gui.py"], "GUI")
    ]

    threads = []
    for cmd_parts, name in components:
        thread = threading.Thread(target=run_script, args=(cmd_parts, name))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    logging.info("All component threads completed their execution attempts.")
