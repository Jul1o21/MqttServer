from src.mqtt_client import init_mqtt, mqtt_message_queue

def main():
    init_mqtt()
    while True:
        if not mqtt_message_queue.empty():
            message = mqtt_message_queue.get()
            if message == "EMPTY":
                print("No hay mensajes detectados")
            else:
                print(f"Mensaje recibido: {message}")

if __name__ == '__main__':
    main()
