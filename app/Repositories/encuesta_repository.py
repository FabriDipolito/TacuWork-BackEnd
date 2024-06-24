import psycopg2

class EncuestaRepository:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                database='Tesis',
                user='postgres',
                password='admin',
                host='localhost',
                port='5432'
            )
        except psycopg2.DatabaseError as e:
            print(f"Error while connecting to PostgreSQL: {e}")

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def create_encuesta(self, respuesta1, respuesta2, respuesta3, comentario, peal_id, nombre):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO ENCUESTAS (respuesta1, respuesta2, respuesta3, comentario, peal_id, nombre)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id, respuesta1, respuesta2, respuesta3, comentario, peal_id, nombre
                """,
                (respuesta1, respuesta2, respuesta3, comentario, peal_id, nombre)
            )
            encuesta = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return encuesta
        except psycopg2.DatabaseError as e:
            print(f"Error while creating Encuesta: {e}")
            return None
        finally:
            self.disconnect()

    def get_encuesta(self, encuesta_id):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(
                """
                SELECT * FROM ENCUESTAS WHERE id = %s
                """,
                (encuesta_id,)
            )
            encuesta = cursor.fetchone()
            cursor.close()
            return encuesta
        except psycopg2.DatabaseError as e:
            print(f"Error while retrieving Encuesta: {e}")
            return None
        finally:
            self.disconnect()

    def update_encuesta(self, encuesta_id, respuesta1, respuesta2, respuesta3, comentario, peal_id):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE ENCUESTAS SET
                respuesta1 = %s,
                respuesta2 = %s,
                respuesta3 = %s,
                comentario = %s,
                peal_id = %s
                WHERE id = %s
                RETURNING id, respuesta1, respuesta2, respuesta3, comentario, peal_id
                """,
                (respuesta1, respuesta2, respuesta3, comentario, peal_id, encuesta_id)
            )
            encuesta = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return encuesta
        except psycopg2.DatabaseError as e:
            print(f"Error while updating Encuesta: {e}")
            return None
        finally:
            self.disconnect()

    def delete_encuesta(self, encuesta_id):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM ENCUESTAS WHERE id = %s",
                (encuesta_id,)
            )
            self.conn.commit()
            cursor.close()
            return encuesta_id
        except psycopg2.DatabaseError as e:
            print(f"Error while deleting Encuesta: {e}")
            return None
        finally:
            self.disconnect()

    def delete_encuestas_by_ids(self, ids):
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = "DELETE FROM ENCUESTAS WHERE id = ANY(%s) RETURNING id"
            cursor.execute(query, (ids,))
            deleted_ids = [row[0] for row in cursor.fetchall()]
            self.conn.commit()
            cursor.close()
            return deleted_ids
        except psycopg2.DatabaseError as e:
            print(f"Error while deleting Encuestas: {e}")
            return []
        finally:
            self.disconnect()

    def get_all_encuestas(self):
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM ENCUESTAS")
            encuestas = cursor.fetchall()
            cursor.close()
            return encuestas
        except psycopg2.DatabaseError as e:
            print(f"Error while retrieving all Encuestas: {e}")
            return []
        finally:
            self.disconnect()