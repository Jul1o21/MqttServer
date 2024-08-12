from src.services.POST.postMessage import postMessage
import time

topic = "prueba"

def topicMessageSub(message):
    # Insertar el mensaje en la base de datos
    postMessage(message)

def topicMessagePub(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic `{topic}`")
        msg_count += 1
