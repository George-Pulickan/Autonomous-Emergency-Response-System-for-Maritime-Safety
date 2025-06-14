import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
# Using a more specific topic for GMDSS data
TOPIC = "gmdss/data"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "GMDSS_Publisher")
client.connect(BROKER)

def generate_gmdss_data():
    """Generates sample GMDSS data."""
    # In a real scenario, this data would come from actual GMDSS equipment
    # or be triggered by specific events.
    message_types = ["DISTRESS", "URGENCY", "SAFETY", "ROUTINE"]
    distress_types = ["FIRE", "FLOODING", "COLLISION", "GROUNDING", "PERSON_OVERBOARD"]

    record_type = random.choice(message_types)
    message_specific_type = "N/A"

    if record_type == "DISTRESS":
        message_specific_type = random.choice(distress_types)
    elif record_type == "URGENCY":
        message_specific_type = "MEDICAL_ASSISTANCE_REQUEST"
    elif record_type == "SAFETY":
        message_specific_type = "WEATHER_WARNING"

    return {
        "record_type": record_type,
        "type": message_specific_type,
        "mmsi": str(random.randint(100000000, 999999999)), # Generate a random 9-digit MMSI
        "latitude": round(random.uniform(-90, 90), 4),    # Random latitude
        "longitude": round(random.uniform(-180, 180), 4), # Random longitude
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime()) # Current UTC time
    }

def publish_gmdss_data(max_messages=5):
    """Publishes a limited number of GMDSS data messages to the MQTT broker."""
    for i in range(max_messages):
        payload = generate_gmdss_data()
        print(f"[MQTT] Publishing GMDSS data ({i+1}/{max_messages}): {payload}")
        client.publish(TOPIC, json.dumps(payload))
        if i < max_messages - 1: # Don't sleep after the last message
            time.sleep(2) # Shortened sleep time for faster testing
    print(f"[MQTT] Finished publishing {max_messages} messages.")
    client.disconnect() # Disconnect after publishing
    print("[MQTT] Disconnected.")


if __name__ == "__main__":
    publish_gmdss_data(5) # Publish 5 messages and exit
