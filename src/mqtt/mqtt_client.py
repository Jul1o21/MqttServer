from paho.mqtt import client as mqtt_client
from mqttconfig import client_id_mq, username_mq, password_mq, broker_mq, port_mq
import threading
import time
import queue

# Importar explícitamente los módulos de tópicos
import src.topics.topicMessage as topicMessage
import src.topics.topicHumedadCalidad as topicHumedadCalidad


mqtt_message_queue = queue.Queue()
last_message_time = time.time()

# Lista explícita de tópicos y sus correspondientes funciones de suscripción y publicación
topics_modules = [
    {"topic": topicMessage.topic, "sub_func": topicMessage.topicMessageSub, "pub_func": topicMessage.topicMessagePub},
    {"topic": topicHumedadCalidad.topic, "sub_func": topicHumedadCalidad.topicHumedadCalidadSub, "pub_func": topicHumedadCalidad.topicHumedadCalidadPub},
]

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            for module in topics_modules:
                client.subscribe(module["topic"])
                print(f"Subscribed to topic `{module['topic']}`")
        else:
            print("Failed to connect, return code %d\n" % rc)
    
    def on_message(client, userdata, msg):
        global last_message_time
        message = msg.payload.decode()
        mqtt_message_queue.put(message)
        last_message_time = time.time()
        print(f"Received `{message}` from `{msg.topic}` topic")
        for module in topics_modules:
            if module["topic"] == msg.topic:
                module["sub_func"](message)

    client = mqtt_client.Client(client_id=client_id_mq, protocol=mqtt_client.MQTTv311, transport="tcp", callback_api_version=mqtt_client.CallbackAPIVersion.VERSION1)
    client.username_pw_set(username_mq, password_mq)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_mq, port_mq)
    return client

def check_for_empty_messages():
    global last_message_time
    while True:
        time.sleep(5)
        if time.time() - last_message_time > 5:
            print("No hay mensajes detectados:", mqtt_message_queue)

def start_mqtt():
    client = connect_mqtt()
    client.loop_start()
    threading.Thread(target=check_for_empty_messages).start()

def init_mqtt():
    mqtt_thread = threading.Thread(target=start_mqtt)
    mqtt_thread.start()
