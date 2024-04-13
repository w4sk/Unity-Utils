import random
import time
import os

from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "/mqtt/urdf/description"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("MQTT Brokerに接続しました")
        else:
            print(f"接続に失敗しました、リターンコード {rc}\n")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish_urdf(client):
    # URDFファイルのパス
    urdf_file_path = 'urdf/crane_plus.urdf'
    # URDFファイルを読み込む
    with open(urdf_file_path, 'r') as file:
        urdf_content = file.read()
    # MQTTでURDFの内容をpublishする
    result = client.publish(topic, urdf_content)
    status = result[0]
    if status == 0:
        print(f"`{topic}`トピックにURDFを送信しました。")
    else:
        print(f"`{topic}`トピックへのメッセージ送信に失敗しました。")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish_urdf(client)

if __name__ == '__main__':
    run()