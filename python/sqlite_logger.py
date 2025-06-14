import sqlite3
import random
import time

conn = sqlite3.connect('gmdss_data.db') # Changed database name
c = conn.cursor()

# Create gmdss_log table
c.execute('''CREATE TABLE IF NOT EXISTS gmdss_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    record_type TEXT,
    type TEXT,
    mmsi TEXT,
    latitude REAL,
    longitude REAL,
    timestamp TEXT
)''')
conn.commit()

# Example GMDSS data (replace with actual data source later)
sample_gmdss_data = {
    "record_type": "DISTRESS",
    "type": "FLOODING",
    "mmsi": "123456789",
    "latitude": 49.2742,
    "longitude": -123.1853, # Corrected longitude for W
    "timestamp": "2025-05-28 12:00 UTC"
}

def log_gmdss_data(data):
    """Logs GMDSS data to the gmdss_log table."""
    try:
        c.execute('''INSERT INTO gmdss_log (record_type, type, mmsi, latitude, longitude, timestamp)
                     VALUES (:record_type, :type, :mmsi, :latitude, :longitude, :timestamp)''', data)
        conn.commit()
        print(f"[SQLite] Logged GMDSS data: {data}")
    except sqlite3.Error as e:
        print(f"[SQLite] Error logging GMDSS data: {e}")

if __name__ == "__main__":
    # This is for example purposes. In a real system, this function would be called by a data processing component.
    log_gmdss_data(sample_gmdss_data)

    # Keep the script running if it's meant to be a long-running logger,
    # or remove if it's just for one-off logging.
    # For now, let's log one sample and then demonstrate querying it.

    # print("\n[SQLite] Querying all GMDSS logs:")
    # c.execute("SELECT * FROM gmdss_log")
    # rows = c.fetchall()
    # for row in rows:
    #     print(row)

    # conn.close() # Connection should be kept open if other modules use it

def main():
    # This is for example purposes. In a real system, this function would be called by a data processing component.
    log_gmdss_data(sample_gmdss_data)

    print("\n[SQLite] Querying all GMDSS logs (if main is run):")
    # Re-establish connection for this standalone test if necessary, or ensure conn is global
    # For simplicity, assuming conn and c are still available if this main is run directly.
    # If run as a standalone script, it might be better to handle connection within main().

    # The global conn and c will be used by log_gmdss_data.
    # If this script is run directly, we might want to close the connection after use.

    try:
        c.execute("SELECT * FROM gmdss_log")
        rows = c.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error querying data in main: {e}")
    finally:
        if conn: # Close connection if main() is executed.
            conn.close()
            print("[SQLite] Connection closed by main().")


if __name__ == "__main__":
    main()
