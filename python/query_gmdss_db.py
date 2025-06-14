import sqlite3

DB_FILE = "gmdss_data.db"

def query_all_data():
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        print(f"Querying all records from gmdss_log in {DB_FILE}:")
        c.execute("SELECT id, record_type, type, mmsi, latitude, longitude, timestamp FROM gmdss_log")
        rows = c.fetchall()

        if not rows:
            print("No data found in gmdss_log table.")
            return

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    query_all_data()
