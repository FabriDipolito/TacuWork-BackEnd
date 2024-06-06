import psycopg2
from psycopg2.extras import RealDictCursor

class UserRepository:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                database='Tesis',
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

    def create_user(self, username, password):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(
                """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
                RETURNING id, username
                """,
                (username, password)
            )
            user = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return user
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def get_user_by_username(self, username):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(
                "SELECT * FROM users WHERE username = %s",
                (username,)
            )
            user = cursor.fetchone()
            cursor.close()
            return user
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def get_user_by_id(self, user_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute(
                "SELECT * FROM users WHERE id = %s",
                (user_id,)
            )
            user = cursor.fetchone()
            cursor.close()
            return user
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

