from config import dbname, host, password, port, user
import psycopg2

class Database:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        db_config = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }
        try:
            self._connection = psycopg2.connect(**db_config)
            print("(SISTEMA)   Conexión exitosa")
        except Exception as e:
            print(f"(SISTEMA)   Error: {e}")
            self._connection = None

    def get_connection(self):
        return self._connection

def get_db_connection():
    db_instance = Database()
    return db_instance.get_connection()
