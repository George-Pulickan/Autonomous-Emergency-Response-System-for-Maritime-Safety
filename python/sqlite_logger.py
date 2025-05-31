import sqlite3
import random
import time

conn = sqlite3.connect('distress_data.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS distress_log (
    timestamp TEXT,
    lat REAL,
    long REAL,
    water_level INTEGER,
    temperature REAL,
    pressure REAL
)''')
conn.commit()

def log_data():
    while True:
        data = {
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "lat": 49.2742,
            "long": -123.1853,
            "water_level": random.randint(30, 100),
            "temperature": round(20 + random.uniform(-5, 5), 2),
            "pressure": round(1013 + random.uniform(-10, 10), 2)
        }
        c.execute("INSERT INTO distress_log VALUES (:timestamp, :lat, :long, :water_level, :temperature, :pressure)", data)
        conn.commit()
        print(f"[SQLite] Logged: {data}")
        time.sleep(10)

if __name__ == "__main__":
    log_data()
