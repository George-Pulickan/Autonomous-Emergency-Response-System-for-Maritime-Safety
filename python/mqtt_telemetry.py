import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
TOPIC = "maritime/distress"

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
