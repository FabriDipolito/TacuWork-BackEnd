from app.Repositories.evaluaciones_repository import EvaluacionesRepository

class EvaluacionesService:
    def __init__(self):
        self.evaluaciones_repository = EvaluacionesRepository()

    def create_evaluacion(self, nombre, comienzo, ultima_actualizacion, peal_id):
        evaluacion = self.evaluaciones_repository.create_evaluacion(nombre, comienzo, ultima_actualizacion, peal_id)

        if evaluacion is None:
            return None

        evaluacion_object = {
            "id": evaluacion[0],
            "nombre": evaluacion[1],
            "comienzo": evaluacion[2],
            "ultima_actualizacion": evaluacion[3],
            "peal_id": evaluacion[4]
        }

        return evaluacion_object

    def get_evaluacion_by_id(self, evaluacion_id):
        return self.evaluaciones_repository.get_evaluacion_by_id(evaluacion_id)

    def update_evaluacion_by_id(self, evaluacion_id, nombre, comienzo, ultima_actualizacion, peal_id):
        updated_evaluacion = self.evaluaciones_repository.update_evaluacion_by_id(evaluacion_id, nombre, comienzo,
                                                                                  ultima_actualizacion, peal_id)

        if updated_evaluacion:
            return {
                "id": updated_evaluacion[0],
                "nombre": updated_evaluacion[1],
                "comienzo": updated_evaluacion[2],
                "ultima_actualizacion": updated_evaluacion[3],
                "peal_id": updated_evaluacion[4]
            }
        else:
            return None

    def delete_evaluacion_by_id(self, evaluacion_id):
        return self.evaluaciones_repository.delete_evaluacion_by_id(evaluacion_id)

    def delete_evaluaciones_by_ids(self, ids):
        return self.evaluaciones_repository.delete_evaluaciones_by_ids(ids)

    def get_evaluaciones_by_peal_id(self, peal_id):
        evaluaciones = self.evaluaciones_repository.get_evaluaciones_by_peal_id(peal_id)

        evaluaciones_json = []

        for evaluacion in evaluaciones:
            evaluacion_dict = {
                "id": evaluacion[0],
                "nombre": evaluacion[1],
                "comienzo": evaluacion[2],
                "ultima_actualizacion": evaluacion[3],
                "peal_id": evaluacion[4]
            }
            evaluaciones_json.append(evaluacion_dict)

        return evaluaciones_json

    def get_all_evaluaciones(self):
        evaluaciones = self.evaluaciones_repository.get_all_evaluaciones()

        evaluaciones_json = []

        for evaluacion in evaluaciones:
            evaluacion_dict = {
                "id": evaluacion[0],
                "nombre": evaluacion[1],
                "comienzo": evaluacion[2],
                "ultima_actualizacion": evaluacion[3],
                "peal_id": evaluacion[4]
            }
            evaluaciones_json.append(evaluacion_dict)

        return evaluaciones_json