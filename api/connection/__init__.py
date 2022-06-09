from .mqtt import Client
import os

broker = os.environ.get('MQTT_BROKER', "broker.mqttdashboard.com")
topic = os.environ.get('MQTT_TOPIC', "test0406")
port = os.environ.get('MQTT_PORT', "1883")

client = Client(broker=broker, topic=topic, port=int(port))