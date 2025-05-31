# 🚢 Autonomous Emergency Response System for Maritime Safety

This project is a full-stack autonomous distress alert system designed for maritime environments. It simulates an intelligent, self-activating safety device capable of detecting water ingress, broadcasting distress messages via VHF and MQTT, logging data locally, and serving real-time updates via a REST API.

Developed using both **C++** and **Python**, the system integrates simulated GPS, sensor fusion, diagnostics, cloud telemetry, and database management.

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

AutonomousMaritimeDistressSystem/

├── src/
│ 
│   ├── gps_tracker.cpp
│ 
│   ├── vhf_radio_sim.cpp
│ 
│   ├── diagnostics.cpp
│ 
│   └── environment_sensor.cpp
│ 
├── python/
│ 
│   ├── water_sensor.py
│ 
│   ├── mqtt_telemetry.py
│ 
│   ├── sqlite_logger.py
│ 
│   ├── rest_api.py
│ 
│   ├── interface_gui.py
│ 
│   └── system_coordinator.py
│ 
├── docs/
│   ├── DEPLOYMENT_GUIDE.md
│ 
│   └── CHECKLIST.md
│ 
├── Makefile
│ 
├── Dockerfile
│ 
├── README.md

