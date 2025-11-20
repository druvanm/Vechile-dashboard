import paho.mqtt.client as mqtt
import random
import time
import json

broker = "broker.hivemq.com"
topic = "myvehicle/can"

# FIX: Use new Callback API (avoids warning)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
client.connect(broker, 1883, 60)

def fake_can():
    return {
        "speed": random.randint(0, 80),
        "temp": random.randint(30, 100),
        "fuel": random.randint(10, 100)
    }

while True:
    packet = fake_can()
    json_data = json.dumps(packet)

    client.publish(topic, json_data)
    print("SENT:", json_data)

    time.sleep(1)
