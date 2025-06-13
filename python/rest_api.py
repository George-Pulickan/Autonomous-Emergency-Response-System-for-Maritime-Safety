from flask import Flask, request, jsonify
import sqlite3
import secrets

app = Flask(__name__)
# IMPORTANT: In a production environment, this token should be read from an environment variable or a secure secrets management system, not hardcoded.
API_TOKEN = secrets.token_urlsafe(32)

@app.before_request
def require_auth():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Authorization header is missing"}), 401

    parts = auth_header.split()

    if parts[0].lower() != 'bearer' or len(parts) == 1 or len(parts) > 2:
        return jsonify({"error": "Invalid token format"}), 401

    token = parts[1]
    if token != API_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

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

