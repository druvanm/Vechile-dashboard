import paho.mqtt.client as mqtt
import json

broker = "broker.hivemq.com"
topic = "myvehicle/can"

# When message arrives
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("RECEIVED:", data)

# FIX: Use the new Callback API Version 2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)

client.on_message = on_message
client.connect(broker, 1883, 60)
client.subscribe(topic)

print("Listening for CAN data...")
client.loop_forever()
