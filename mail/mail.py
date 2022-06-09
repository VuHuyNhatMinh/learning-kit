import paho.mqtt.client as mqtt
import json
import os

class Customer():
    def __init__(self, broker, topic, port):
        print("Init")
        self.broker = broker
        self.topic = topic
        self.port = port
        self.conn = mqtt.Client()
        self.conn.on_connect = self.on_connect
        self.conn.on_connect_fail = self.on_connect_fail
        self.conn.on_message = self.on_message
        # self.conn.username_pw_set(username='MinhVHN', password='1')
        self.conn.connect(self.broker, self.port, 60)
    
    def on_connect(self, client, userdata, flags, rc):
        print("Connected")

    def on_connect_fail(self):
        print("Disconnected")   

    def on_message(self, client, userdata, msg):
        print(json.loads(msg.payload))

    def subcribe(self):
        print(f'Topic: {self.topic}')
        self.conn.subscribe(self.topic)
        self.conn.loop_forever()

def main():
    broker = os.environ.get('MQTT_BROKER', "broker.mqttdashboard.com")
    print(broker)
    topic = os.environ.get('MQTT_TOPIC', "test0406")
    port = os.environ.get('MQTT_PORT', '1883')
    customer = Customer(broker=broker, topic=topic, port=int(port))
    customer.subcribe()

if __name__ == '__main__':
    main()