import psycopg2

class ColaboradoresRepository:
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
            print(self.conn)
            self.conn.close()

    def create_colaborador(self, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos,
                           peal_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO COLABORADORES (nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_colaborador_by_id(self, colaborador_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM COLABORADORES WHERE id = %s",
                (colaborador_id,)
            )
            colaborador = cursor.fetchone()
            cursor.close()
            return colaborador
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_colaborador_by_id(self, colaborador_id, nombre, apellido, edad, hijos, zona_residencial, telefono,
                                 nivel_educativo, egresos, peal_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE COLABORADORES SET nombre = %s, apellido = %s, edad = %s, hijos = %s, zona_residencial = %s, telefono = %s, nivel_educativo = %s, egresos = %s, peal_id = %s WHERE id = %s",
                (nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id,
                 colaborador_id)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def delete_colaborador_by_id(self, colaborador_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "DELETE FROM COLABORADORES WHERE id = %s",
                (colaborador_id,)
            )
            self.conn.commit()
            cursor.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_all_colaboradores(self):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM COLABORADORES")
            colaboradores = cursor.fetchall()
            cursor.close()
            return colaboradores
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def get_colaboradores_by_peal_id(self, peal_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM COLABORADORES WHERE peal_id = %s",
                (peal_id,)
            )
            colaboradores = cursor.fetchall()
            cursor.close()
            return colaboradores
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)