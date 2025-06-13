# 🚢 Autonomous Emergency Response System for Maritime Safety

This project simulates an autonomous distress alert system designed for maritime environments. It aims to model an intelligent, self-activating safety device capable of detecting simulated water ingress, broadcasting distress messages via MQTT, logging data locally, and serving recent event updates via a REST API.

Developed using both **C++** and **Python**, the system integrates simulated GPS data parsing, environmental sensor simulation, system diagnostics, MQTT telemetry, local database logging, a REST API, and a basic manual trigger GUI.

---

## 🧠 Features

- ✅ Real-time GPS data parsing (C++ - `src/gps_tracker.cpp`)
- ✅ Environmental sensor simulation (C++ - `src/environment_sensor.cpp`)
- ✅ System diagnostics module (C++ - `src/diagnostics.cpp`)
- ✅ Water ingress detection simulation (Python - `python/water_sensor.py`)
- ✅ MQTT-based telemetry to a public broker (Python - `python/mqtt_telemetry.py`)
- ✅ SQLite local logging for distress events (Python - `python/sqlite_logger.py`)
- ✅ Flask REST API serving last 10 events with token authentication (Python - `python/rest_api.py`)
- ✅ Basic Tkinter GUI for manual distress trigger (Python - `python/interface_gui.py`)
- ✅ Centralized system orchestration (Python - `python/system_coordinator.py`)
- 📝 VHF distress signal simulation (Planned)
- 📝 Dockerfile for containerization (Planned)
- 📝 GitHub Actions CI workflow support (Planned)

---

## 🗂 Project Structure

- `README.md` - This file.
- `Basic GMDSS Data Format (Simplified Example)` - Document outlining a simplified GMDSS data structure.
- `Example JSON response` - Example of the JSON output from the REST API.
- `Frontend Dashboard (React)` - Placeholder or concept note for a React-based frontend.
- `SMS/` - Directory related to planned SMS/Email alert functionalities.
  - `Email Alerts (Twilio + SMTP)` - Placeholder or concept note.
  - `SMS (using Twilio)` - Placeholder or concept note.
- `python/` - Contains Python scripts for various system components.
  - `interface_gui.py` - Tkinter GUI for manual distress signal.
  - `mqtt_telemetry.py` - Publishes simulated telemetry data via MQTT.
  - `rest_api.py` - Flask REST API to serve recent log data.
  - `sqlite_logger.py` - Logs simulated data to an SQLite database.
  - `system_coordinator.py` - Orchestrates the startup and management of all system components.
  - `water_sensor.py` - Simulates a water level sensor and triggers alerts.
- `src/` - Contains C++ source code for core functionalities.
  - `diagnostics.cpp` - System diagnostics utility.
  - `environment_sensor.cpp` - Simulates environmental sensor readings.
  - `gps_tracker.cpp` - Parses NMEA $GPGGA GPS sentences.

---

## 🧰 Prerequisites

Install these tools:

| Tool     | Install Command                          | Notes                                                                                                                             |
|----------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Python 3 | `sudo apt install python3 python3-pip`    | Required for all Python scripts.                                                                                                  |
| pip      | `sudo apt install python3-pip`            | Python package installer.                                                                                                         |
| g++      | `sudo apt install g++`                    | GNU C++ compiler, needed for C++ components.                                                                                      |
| make     | `sudo apt install make`                   | (A Makefile is not provided in the root directory; C++ components may need manual compilation, e.g., for diagnostics: `g++ -std=c++11 -o diag_proc src/diagnostics.cpp`) |

---

## ⚙️ Setup Instructions

### 1. Clone or Extract Repository
If you cloned from a version control system:
```bash
# Example: git clone <repository-url>
# cd <repository-name>
```
Ensure all files are in their respective directories as per the "Project Structure" section.

### 2. Install Python Dependencies
```bash
pip install flask paho-mqtt
```
Note: `twilio` can be installed if you plan to implement the SMS alert functionality.

### 3. Compile C++ Code
Compile C++ components. For example, to compile the diagnostics tool:
```bash
g++ -std=c++11 -o diag_proc src/diagnostics.cpp
```
(Ensure this executable is in the root directory (`./diag_proc`) or adjust the path in `python/system_coordinator.py` if placed elsewhere, e.g. `build/diag_proc`). Other C++ components (`environment_sensor.cpp`, `gps_tracker.cpp`) are currently illustrative and not directly executed by the coordinator but their logic is explained in their respective subtask reports.

### 4. Run Entire System
Launch the system coordinator:
```bash
python3 python/system_coordinator.py
```
This starts the following components in parallel:
- ./diag_proc (System Diagnostics)
- Water Sensor Simulator (`python/water_sensor.py`)
- MQTT Telemetry Publisher (`python/mqtt_telemetry.py`)
- SQLite Logger (`python/sqlite_logger.py`)
- Flask REST API (`python/rest_api.py`)
- Manual Distress Trigger GUI (`python/interface_gui.py`)

Monitor the console output from `system_coordinator.py` for status updates, component outputs, and any errors.

---

## 📡 MQTT Telemetry
- **Broker:** `test.mosquitto.org` (Public test broker - **not for production use**)
- **Topic:** `maritime/distress`
- **Format:** JSON telemetry published approximately every 5 seconds by `mqtt_telemetry.py`.
- **Example Payload:** `{"lat": 49.2742, "long": -123.1853, "water_level": <random_int>, "temperature": <random_float>, "pressure": <random_float>}`

---

## 📬 Email & SMS Alerts (Planned Feature)

The system is designed with future integration of email and SMS alerts in mind. Placeholder files/concepts exist in the `SMS/` directory.

Currently, scripts like `email_alerts.py` or `sms_alerts.py` are **not provided** in the `python/` directory and are not integrated into `system_coordinator.py`.

**To implement this feature:**
1.  Develop Python scripts (e.g., `python/email_alerts.py`, `python/sms_alerts.py`) using libraries like `smtplib` (for email) and a third-party SMS gateway provider's API (e.g., Twilio, Vonage).
2.  Securely manage credentials for these services (e.g., using environment variables or a secrets management system).
3.  Modify `python/system_coordinator.py` or individual components (like `python/water_sensor.py`) to call these alerting scripts when specific conditions are met (e.g., high water level, manual distress signal).

---

## 📄 Log Files Generated

- `system_diagnostics.log`: Logged by `src/diagnostics.cpp`. Contains system status checks.
- `water_log.txt`: Logged by `python/water_sensor.py`. Records instances where simulated water level exceeds the threshold.
- `distress_data.db`: SQLite database file created and managed by `python/sqlite_logger.py`. Stores time-series data of simulated distress events.
- `manual_trigger.log`: Logged by `python/interface_gui.py` when the manual distress button is pressed.

Check these files for diagnostics and event history. The `system_coordinator.py` will also print much of this information to its console output.
