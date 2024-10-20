import os
from dotenv import load_dotenv

import psycopg2
from psycopg2.extras import RealDictCursor

class UserRepository:
    def __init__(self):
        self.conn = None

    def connect(self):
        load_dotenv()

        database = os.getenv('DB_DATABASE')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')

        try:
            self.conn = psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port,
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

