import psycopg2
# from app.config import db_config


class PealRepository:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            # params = db_config()
            self.conn = psycopg2.connect(database='Tesis',
                                         user='postgres',
                                         password='admin',
                                         host='localhost',
                                         port='5432',
                                         )
            print(self.conn)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def create_peal(self, nombre, comienzo, fin):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO PEAL (nombre, comienzo, fin) VALUES (%s, %s, %s)",
                (nombre, comienzo, fin)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_peal_by_id(self, peal_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM PEAL WHERE id = %s",
                (peal_id,)
            )
            peal = cursor.fetchone()
            cursor.close()
            return peal
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_peal_by_id(self, peal_id, nombre, comienzo, fin):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE PEAL SET nombre = %s, comienzo = %s, fin = %s WHERE id = %s",
                (nombre, comienzo, fin, peal_id)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_peal_by_id(self, peal_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM PEAL WHERE id = %s",
                (peal_id,)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_all_peals(self):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM PEAL")
            peals = cursor.fetchall()
            cursor.close()
            return peals
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
