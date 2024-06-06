from app.Repositories.puntajes_repository import PuntajesRepository

class PuntajesService:
    def __init__(self):
        self.puntajes_repository = PuntajesRepository()

    def create_puntaje(self, colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
                       comunicacion, liderazgo, proactividad, presencia, puntualidad,
                       porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral):
        puntaje = self.puntajes_repository.create_puntaje(
            colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
            comunicacion, liderazgo, proactividad, presencia, puntualidad,
            porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral
        )

        if puntaje is None:
            return None

        puntaje_object = {
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
        }

        return puntaje_object

    def get_puntaje(self, colaborador_id, evaluacion_id):
        return self.puntajes_repository.get_puntaje(colaborador_id, evaluacion_id)

    def update_puntaje(self, colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
                       comunicacion, liderazgo, proactividad, presencia, puntualidad,
                       porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral):
        puntaje = self.puntajes_repository.update_puntaje(
            colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
            comunicacion, liderazgo, proactividad, presencia, puntualidad,
            porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral
        )

        if puntaje is None:
            return None

        puntaje_object = {
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
        }

        return puntaje_object

    def delete_puntaje(self, colaborador_id, evaluacion_id):
        return self.puntajes_repository.delete_puntaje(colaborador_id, evaluacion_id)

    def delete_puntajes_by_ids(self, colaborador_ids, evaluacion_ids):
        return self.puntajes_repository.delete_puntajes_by_ids(colaborador_ids, evaluacion_ids)

    def get_all_puntajes(self):
        return self.puntajes_repository.get_all_puntajes()
