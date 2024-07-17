from src.database.db import get_db_connection

def postMessage(contenido):
    try:
        conn = get_db_connection()
        inst = '''
                INSERT INTO mensajes (contenido)
                VALUES (%(contenido)s);
               '''
        with conn.cursor() as cursor:
            cursor.execute(inst, {'contenido': contenido})
            conn.commit()
            cursor.close()
        print("Mensaje insertado en la base de datos.")
    except Exception as e:
        print("(SISTEMA)   Error: "+str(e))
        return ''