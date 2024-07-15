from src.mqtt_client import init_mqtt, mqtt_message_queue

def init_app():
    init_mqtt()
    return mqtt_message_queue
