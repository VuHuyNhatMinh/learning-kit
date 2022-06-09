import paho.mqtt.client as mqtt

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Client(metaclass=SingletonMeta):
    def __init__(self):
        print("Init1")

    def __init__(self, broker, topic, port):
        print("Init2")
        self.broker = broker
        self.topic = topic
        self.port = port
        self.conn = mqtt.Client()
        self.conn.on_connect = self.on_connect
        self.conn.on_connect_fail = self.on_connect_fail
        self.conn.on_publish = self.on_publish
        # self.conn.username_pw_set(username='MinhVHN', password='1')
        self.conn.connect(self.broker, self.port, 60)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected")

    def on_connect_fail(self):
        print("Disconnected")

    def on_publish(self, client, userdata, mid):
        print("Success")

    def publish(self, payload):
        print("--mqtt--")
        print(payload)
        print(self.topic)
        self.conn.loop_start()
        self.conn.publish(self.topic, payload)
        self.conn.loop_stop()
