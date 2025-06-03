# 🚢 Autonomous Emergency Response System for Maritime Safety

This project is a full-stack autonomous distress alert system designed for maritime environments. It simulates an intelligent, self-activating safety device capable of detecting water ingress, broadcasting distress messages via VHF and MQTT, logging data locally, and serving real-time updates via a REST API.

Developed using both **C++** and **Python**, the system integrates simulated GPS, sensor fusion, diagnostics, cloud telemetry, and database management.

If interested in blueprints of plans and parts used, please email me at pulickan06@gmail.com, for more information.

---

## 🧠 Features

- ✅ Real-time GPS data parsing (C++)
- ✅ Water ingress detection (Python)
- ✅ VHF distress signal simulation (C++)
- ✅ MQTT-based telemetry to public broker
- ✅ SQLite local logging for analytics
- ✅ Flask REST API serving last 10 events
- ✅ GUI for manual distress trigger (Python Tkinter)
- ✅ Full orchestration via coordinator script
- ✅ Dockerfile for containerization
- ✅ GitHub Actions CI workflow support

---

## 🗂 Project Structure

- ├── src/                            # C++ modules
- ├── python/
- │   ├── water_sensor.py
- │   ├── mqtt_telemetry.py
- │   ├── sqlite_logger.py
- │   ├── rest_api.py                 # now includes token auth
- │   ├── email_alerts.py             # NEW
- │   ├── sms_alerts.py               # NEW
- │   └── system_coordinator.py
- ├── dashboard-react/                # React frontend
- │   └── src/App.js
- ├── Dockerfile
- ├── Makefile
- ├── requirements.txt
- ├── setup.py
- ├── README.md
- ├── docs/
- │   ├── DEPLOYMENT_GUIDE.md
- │   └── CHECKLIST.md
- └── .github/workflows/ci.yml




---

## 🧰 Prerequisites

Install these tools:

| Tool     | Install Command                          |
|----------|-------------------------------------------|
| Python 3 | `sudo apt install python3 python3-pip`    |
| pip      | `sudo apt install python3-pip`            |
| g++      | `sudo apt install g++`                    |
| make     | `sudo apt install make`                   |
| Docker   | [Install Docker](https://docs.docker.com/get-docker/) (optional)

---

## ⚙️ Setup Instructions

### 1. Clone or Extract

Clone from GitHub:
```bash
git clone https://github.com/your-username/AutonomousMaritimeDistressSystem.git
cd AutonomousMaritimeDistressSystem
```
### 2. Install Python Dependencies

pip install flask paho-mqtt twilio

### 3. Compile C++ Code
bash make
### 4. Run Entire System
bash python3 python/system_coordinator.py

This starts:
- Water sensor simulator

- MQTT publisher

- SQLite logger

- Flask REST API

- Manual GUI interface


### 5.🌐 Accessing REST API
Visit:
http://localhost:5000/api/logs

If using token auth:

makefile
Authorization: Bearer secret123


### 6.📡 MQTT Telemetry
Broker: test.mosquitto.org

Topic: maritime/distress

Format: JSON telemetry every 5s


### 7.📬 Email & SMS Alerts
Configure your credentials in email_alerts.py and sms_alerts.py

Run them manually or integrate into system_coordinator.py



