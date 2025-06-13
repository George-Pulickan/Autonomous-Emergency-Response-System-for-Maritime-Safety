import random
import time

THRESHOLD = 70
LOG_FILE = "water_log.txt"

def read_water_level():
    return random.randint(30, 100)

def log_event(level):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - ALERT - High water level detected: {level}\n")

def monitor_water_level():
    while True:
        level = read_water_level()
        print(f"[Sensor] Current water level: {level}")
        if level > THRESHOLD:
            print("[ALERT] Water ingress detected! Sending distress signal...")
            log_event(level)
            break
        time.sleep(2)

if __name__ == "__main__":
    monitor_water_level()
