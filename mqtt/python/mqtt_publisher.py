import random
import time
import os
import threading
import json

from paho.mqtt import client as mqtt_client

class MQTTPublisher:
    def __init__(self, broker='192.168.207.159', port=1883, topic='echo'):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = f'python-mqtt-{random.randint(0, 100)}'
        # self.username = 'emqx'
        # self.password = 'public'
        self.client = self.connect_mqtt()

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        # client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    # def publish(self, msg_count=0):
    #     time.sleep(1)  # このスリープは必要に応じて調整してください。
    #     # msg = f"messages: {msg_count}"
    #     msg =  '"message": "Hello"'
    #     result = self.client.publish(self.topic, msg)
    #     status = result[0]
    #     if status == 0:
    #         print(f"Send `{msg}` to topic `{self.topic}`")
    #     else:
    #         print(f"Failed to send message to topic {self.topic}")
    #     threading.Timer(1, self.publish, args=(msg_count+1,)).start()  # 1秒後に再度publishを呼び出す
    
    
    import json  # jsonモジュールをインポート

    def publish(self, msg_count=0):
        time.sleep(1)  # このスリープは必要に応じて調整してください。
        msg_dict = {"data": "Hello"}  # メッセージを辞書として定義
        msg = json.dumps(msg_dict)  # 辞書をJSON文字列に変換
        result = self.client.publish(self.topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{self.topic}`")
        else:
            print(f"Failed to send message to topic {self.topic}")
        threading.Timer(1, self.publish, args=(msg_count+1,)).start()  # 1秒後に再度publishを呼び出す

    def run(self):
        self.publish()


if __name__ == '__main__':
    publisher = MQTTPublisher()
    publisher.run()
