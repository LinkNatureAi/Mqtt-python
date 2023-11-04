import paho.mqtt.client as mqtt
import random
import time

# Define the MQTT client
client = mqtt.Client()

# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  # Subscribe to the topic "train"
  client.subscribe("train")

# Define the callback function for when the client receives a message
def on_message(client, userdata, msg):
  print("Received message: " + msg.topic + " -> " + msg.payload.decode())

# Connect to the HiveMQ broker
client.connect("broker.hivemq.com", 1883, 60)

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Start the loop to process MQTT messages
client.loop_start()

# Publish a random number to the topic "train" every 3 seconds
while True:
  random_number = random.randint(1, 100)
  client.publish("train2", str(random_number))
  time.sleep(3)
