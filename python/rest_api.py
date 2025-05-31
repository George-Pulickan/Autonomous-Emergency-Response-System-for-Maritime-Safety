from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/logs', methods=['GET'])
def get_logs():
    conn = sqlite3.connect('distress_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM distress_log ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([
        {"timestamp": row[0], "lat": row[1], "long": row[2], "water_level": row[3], "temperature": row[4], "pressure": row[5]}
        for row in rows
    ])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
