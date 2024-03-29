import random
import time
import os

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    from datetime import datetime

    def publish(client):
        msg_count = 0
        max_byte_msg =  msg = os.urandom(128 * 1024)  # 128KBのランダムバイナリデータ
        result = client.publish(topic, max_byte_msg)
        status = result[0]
        if status == 0:
            print(datetime.now().strftime('%H:%M:%S.%f'))
        else:
            print(f"Failed to send message to topic {topic}")
        while True:
            time.sleep(1)
            msg = f"messages: {msg_count}"
            current_time = datetime.now().strftime('%H:%M:%S.%f')
            msg_with_time = f"{msg} at {current_time}"
            result = client.publish(topic, msg_with_time)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg_with_time}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            msg_count += 1

    publish(client)


if __name__ == '__main__':
    run()