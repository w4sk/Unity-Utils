import random

from paho.mqtt import client as mqtt_client


class MQTTSubscriber:
  def __init__(self, broker='localhost', port=1883, topic="python/mqtt"):
    self.broker = broker
    self.port = port
    self.topic = topic
    self.client_id = f'python-mqtt-{random.randint(0, 100)}'
    # self.username = 'emqx'
    # self.password = 'public'
    self.client = self.connect_mqtt()
  
  def connect_mqtt(self) -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
      if rc == 0:
        print("Connected to MQTT Broker!")
      else:
        print("Failed to connect, return code %d\n", rc)
    
    client = mqtt_client.Client(self.client_id)
    # client.username_pw_set(self.username, self.password)
    client.on_connect = on_connect
    client.connect(self.broker, self.port)
    return client
  
  def subscribe(self):
    def on_message(client, userdata, msg):
      try:
        print(f"Received `{msg.payload.decode('utf-8')}` from `{msg.topic}` topic")
      except UnicodeDecodeError:
        print("Received message with non-utf-8 encoded payload")
    
    self.client.subscribe(self.topic)
    self.client.on_message = on_message
  
  def run(self):
    self.subscribe()
    self.client.loop_forever()

if __name__ == '__main__':
  subscriber = MQTTSubscriber()
  subscriber.run()
