import base64

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
                           peal_id, comienzo=None, finalizacion=None):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO COLABORADORES (nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id, comienzo, finalizacion)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id, comienzo, finalizacion)
            )
            colaborador_id = cursor.fetchone()[0]
            self.conn.commit()

            cursor.execute(
                "SELECT * FROM COLABORADORES WHERE id = %s",
                (colaborador_id,)
            )
            colaborador = cursor.fetchone()
            cursor.close()
            return colaborador
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

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
                                 nivel_educativo, egresos, peal_id, banco=None, sucursal=None, numero_cuenta=None,
                                 nombre_emergencia=None, telefono_emergencia=None, imagen=None, comienzo=None,
                                 finalizacion=None):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()

            set_clauses = [
                "nombre = %s",
                "apellido = %s",
                "edad = %s",
                "hijos = %s",
                "zona_residencial = %s",
                "telefono = %s",
                "nivel_educativo = %s",
                "egresos = %s",
                "peal_id = %s",
                "banco = COALESCE(%s, banco)",
                "sucursal = COALESCE(%s, sucursal)",
                "numero_cuenta = COALESCE(%s, numero_cuenta)",
                "nombre_emergencia = COALESCE(%s, nombre_emergencia)",
                "telefono_emergencia = COALESCE(%s, telefono_emergencia)",
                "comienzo = COALESCE(%s::DATE, comienzo)",
                "finalizacion = COALESCE(%s::DATE, finalizacion)"
            ]

            params = [
                nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id,
                banco, sucursal, numero_cuenta, nombre_emergencia, telefono_emergencia, comienzo, finalizacion
            ]

            if imagen:
                imagen_bytes = imagen.read()
                set_clauses.append("imagen = %s")
                params.append(imagen_bytes)

            sql = f"""
                UPDATE COLABORADORES SET 
                    {', '.join(set_clauses)}
                WHERE id = %s
                RETURNING id, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id, imagen, banco, sucursal, numero_cuenta, nombre_emergencia, telefono_emergencia, comienzo, finalizacion
            """
            params.append(colaborador_id)

            cursor.execute(sql, params)
            updated_colaborador = cursor.fetchone()
            self.conn.commit()
            cursor.close()

            return updated_colaborador
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

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

    def delete_colaboradores_by_ids(self, ids):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            query = "DELETE FROM COLABORADORES WHERE id = ANY(%s) RETURNING id"
            cursor.execute(query, (ids,))
            deleted_ids = [row[0] for row in cursor.fetchall()]
            self.conn.commit()
            cursor.close()
            return deleted_ids
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return []

    def get_all_colaboradores(self):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT id, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id, imagen, banco, sucursal, numero_cuenta, nombre_emergencia, telefono_emergencia, comienzo, finalizacion FROM COLABORADORES"
            )
            colaboradores = cursor.fetchall()
            cursor.close()
            return colaboradores
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

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