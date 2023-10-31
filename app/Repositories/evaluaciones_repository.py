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
                "INSERT INTO EVALUACIONES (nombre, comienzo, ultima_actualizacion, peal_id) VALUES (%s, %s, %s, %s)",
                (nombre, comienzo, ultima_actualizacion, peal_id)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

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
                "UPDATE EVALUACIONES SET nombre = %s, comienzo = %s, ultima_actualizacion = %s, peal_id = %s WHERE id = %s",
                (nombre, comienzo, ultima_actualizacion, peal_id, evaluacion_id)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_evaluacion_by_id(self, evaluacion_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM EVALUACIONES WHERE id = %s",
                (evaluacion_id,)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

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