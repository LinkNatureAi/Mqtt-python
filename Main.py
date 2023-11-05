import paho.mqtt.client as mqtt
import random
import time

# Define the MQTT client
client = mqtt.Client()

# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print("Connected successfully")
    # Subscribe to the topic "train"
    client.subscribe("train")
  else:
    print("Connection failed with code " + str(rc))

# Define the callback function for when the client receives a message
def on_message(client, userdata, msg):
  try:
    print("Received message: " + msg.topic + " -> " + msg.payload.decode())
  except Exception as e:
    print("Error handling message:", e)

# Define the callback function for when there's an error
def on_error(client, userdata, rc):
  print("Error: " + str(rc))

# Connect to the HiveMQ broker with error handling
try:
  client.on_connect = on_connect
  client.on_message = on_message
  client.on_error = on_error
  client.connect("broker.hivemq.com", 1883, 60)
  client.loop_start()

  # Publish a random number to the topic "train" every 3 seconds
  while True:
    random_number = random.randint(1, 100)
    client.publish("train2", str(random_number))
    time.sleep(0.5)

except Exception as e:
  print("Error:", e)
  client.disconnect()
