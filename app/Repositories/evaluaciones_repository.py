import psycopg2

class EvaluacionesRepository:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(database='Tesis',
                                         user='postgres',
                                         password='admin',
                                         host='localhost',
                                         port='5432',
                                         )
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def create_evaluacion(self, nombre, comienzo, ultima_actualizacion, peal_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO EVALUACIONES (nombre, comienzo, ultima_actualizacion, peal_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id, nombre, comienzo, ultima_actualizacion, peal_id
                """,
                (nombre, comienzo, ultima_actualizacion, peal_id)
            )
            evaluacion = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return evaluacion
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def get_evaluacion_by_id(self, evaluacion_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM EVALUACIONES WHERE id = %s",
                (evaluacion_id,)
            )
            evaluacion = cursor.fetchone()
            cursor.close()
            return evaluacion
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_evaluacion_by_id(self, evaluacion_id, nombre, comienzo, ultima_actualizacion, peal_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE EVALUACIONES SET 
                    nombre = %s, 
                    comienzo = %s, 
                    ultima_actualizacion = %s, 
                    peal_id = %s 
                WHERE id = %s
                RETURNING id, nombre, comienzo, ultima_actualizacion, peal_id
                """,
                (nombre, comienzo, ultima_actualizacion, peal_id, evaluacion_id)
            )
            updated_evaluacion = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return updated_evaluacion
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_evaluacion_by_id(self, evaluacion_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM EVALUACIONES WHERE id = %s RETURNING id",
                (evaluacion_id,)
            )
            deleted_id = cursor.fetchone()[0]
            self.conn.commit()
            cursor.close()
            return deleted_id
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def delete_evaluaciones_by_ids(self, ids):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            query = "DELETE FROM EVALUACIONES WHERE id = ANY(%s) RETURNING id"
            cursor.execute(query, (ids,))
            deleted_ids = [row[0] for row in cursor.fetchall()]
            self.conn.commit()
            cursor.close()
            return deleted_ids
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return []

    def get_evaluaciones_by_peal_id(self, peal_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM EVALUACIONES WHERE peal_id = %s",
                (peal_id,)
            )
            evaluaciones = cursor.fetchall()
            cursor.close()
            return evaluaciones
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_all_evaluaciones(self):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM EVALUACIONES")
            evaluaciones = cursor.fetchall()
            cursor.close()
            return evaluaciones
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)