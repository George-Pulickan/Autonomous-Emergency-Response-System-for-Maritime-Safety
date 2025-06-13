import json
import time
import random
import paho.mqtt.client as mqtt

# IMPORTANT: test.mosquitto.org is a public test broker.
# It is not suitable for production use due to lack of security (unencrypted,
# no authentication) and reliability (no uptime guarantees, data can be accessed by anyone).
BROKER = "test.mosquitto.org"
TOPIC = "maritime/distress"
# For a production environment, MQTT broker details (address, port, credentials if any,
# and topic) should be configurable, for example, via environment variables or a
# dedicated configuration file, rather than being hardcoded.

client = mqtt.Client("MaritimeTelemetry")
client.connect(BROKER)

def generate_data():
    return {
        "lat": 49.2742,
        "long": -123.1853,
        "water_level": random.randint(40, 100),
        "temperature": round(20 + random.uniform(-5, 5), 2),
        "pressure": round(1013 + random.uniform(-10, 10), 2)
    }

def publish_data():
    while True:
        payload = generate_data()
        print(f"[MQTT] Publishing: {payload}")
        client.publish(TOPIC, json.dumps(payload))
        time.sleep(5)

if __name__ == "__main__":
    publish_data()
