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
                "INSERT INTO PEAL (nombre, comienzo, fin) VALUES (%s, %s, %s) RETURNING id, nombre, comienzo, fin",
                (nombre, comienzo, fin)
            )
            peal = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return peal
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

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
                """
                UPDATE PEAL SET 
                    nombre = %s, 
                    comienzo = %s, 
                    fin = %s 
                WHERE id = %s
                RETURNING id, nombre, comienzo, fin
                """,
                (nombre, comienzo, fin, peal_id)
            )
            updated_peal = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return updated_peal
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

    def delete_peales_by_ids(self, ids):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            query = "DELETE FROM PEAL WHERE id = ANY(%s) RETURNING id"
            cursor.execute(query, (ids,))
            deleted_ids = [row[0] for row in cursor.fetchall()]
            self.conn.commit()
            cursor.close()
            return deleted_ids
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return []

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
