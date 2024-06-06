import psycopg2

class PuntajesRepository:
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

    def create_puntaje(self, colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
                       comunicacion, liderazgo, proactividad, presencia, puntualidad,
                       porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                """
                INSERT INTO PUNTAJES (
                    colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales, 
                    comunicacion, liderazgo, proactividad, presencia, puntualidad, 
                    porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales, 
                          comunicacion, liderazgo, proactividad, presencia, puntualidad, 
                          porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral
                """,
                (
                    colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
                    comunicacion, liderazgo, proactividad, presencia, puntualidad,
                    porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral
                )
            )
            puntaje = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return puntaje
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def get_puntaje(self, colaborador_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM PUNTAJES WHERE colaborador_id = %s",
                (colaborador_id,)
            )
            puntajes = cursor.fetchall()
            cursor.close()

            puntajes_json = []
            for puntaje in puntajes:
                puntaje_dict = {
                    "colaborador_id": puntaje[0],
                    "evaluacion_id": puntaje[1],
                    "adaptacion_al_cambio": puntaje[2],
                    "habilidades_relacionales": puntaje[3],
                    "comunicacion": puntaje[4],
                    "liderazgo": puntaje[5],
                    "proactividad": puntaje[6],
                    "presencia": puntaje[7],
                    "puntualidad": puntaje[8],
                    "porcentaje_asistencia": puntaje[9],
                    "trabajo_en_equipo": puntaje[10],
                    "responsabilidades": puntaje[11],
                    "rendimiento_laboral": puntaje[12],
                }
                puntajes_json.append(puntaje_dict)

            return puntajes_json
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def update_puntaje(self, colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
                       comunicacion, liderazgo, proactividad, presencia, puntualidad,
                       porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                """
                UPDATE PUNTAJES SET 
                    adaptacion_al_cambio = %s,
                    habilidades_relacionales = %s,
                    comunicacion = %s,
                    liderazgo = %s,
                    proactividad = %s,
                    presencia = %s,
                    puntualidad = %s,
                    porcentaje_asistencia = %s,
                    trabajo_en_equipo = %s,
                    responsabilidades = %s,
                    rendimiento_laboral = %s
                WHERE colaborador_id = %s AND evaluacion_id = %s
                RETURNING colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales, 
                          comunicacion, liderazgo, proactividad, presencia, puntualidad, 
                          porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral
                """,
                (
                    adaptacion_al_cambio, habilidades_relacionales, comunicacion, liderazgo, proactividad,
                    presencia, puntualidad, porcentaje_asistencia, trabajo_en_equipo, responsabilidades,
                    rendimiento_laboral, colaborador_id, evaluacion_id
                )
            )
            puntaje = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return puntaje
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def delete_puntaje(self, colaborador_id, evaluacion_id):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute(
                """
                DELETE FROM PUNTAJES 
                WHERE colaborador_id = %s AND evaluacion_id = %s
                RETURNING colaborador_id, evaluacion_id
                """,
                (colaborador_id, evaluacion_id)
            )
            deleted_record = cursor.fetchone()
            self.conn.commit()
            cursor.close()
            return deleted_record
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return None

    def delete_puntajes_by_ids(self, colaborador_ids, evaluacion_ids):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()

            deleted_records = []
            for colaborador_id, evaluacion_id in zip(colaborador_ids, evaluacion_ids):
                cursor.execute(
                    """
                    DELETE FROM PUNTAJES 
                    WHERE colaborador_id = %s AND evaluacion_id = %s
                    RETURNING colaborador_id, evaluacion_id
                    """,
                    (colaborador_id, evaluacion_id)
                )
                result = cursor.fetchone()
                if result:
                    deleted_records.append({"colaborador_id": result[0], "evaluacion_id": result[1]})

            self.conn.commit()
            cursor.close()
            return deleted_records
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return []

    def get_all_puntajes(self):
        try:
            if self.conn is None:
                self.connect()

            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM PUNTAJES")
            puntajes = cursor.fetchall()
            cursor.close()

            puntajes_json = []

            for puntaje in puntajes:
                puntaje_dict = {
                    "colaborador_id": puntaje[0],
                    "evaluacion_id": puntaje[1],
                    "adaptacion_al_cambio": puntaje[2],
                    "habilidades_relacionales": puntaje[3],
                    "comunicacion": puntaje[4],
                    "liderazgo": puntaje[5],
                    "proactividad": puntaje[6],
                    "presencia": puntaje[7],
                    "puntualidad": puntaje[8],
                    "porcentaje_asistencia": puntaje[9],
                    "trabajo_en_equipo": puntaje[10],
                    "responsabilidades": puntaje[11],
                    "rendimiento_laboral": puntaje[12]
                    # Agrega el resto de los campos aquí...
                }
                puntajes_json.append(puntaje_dict)

            return puntajes_json

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
