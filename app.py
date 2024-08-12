from src.mqtt.mqtt_client import init_mqtt, mqtt_message_queue

def main():
    init_mqtt()
    while True:
        if not mqtt_message_queue.empty():
            message = mqtt_message_queue.get()
            #if message != "EMPTY":

if __name__ == '__main__':
    main()
