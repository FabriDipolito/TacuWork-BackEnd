from app.Repositories.evaluaciones_repository import EvaluacionesRepository

class EvaluacionesService:
    def __init__(self):
        self.evaluaciones_repository = EvaluacionesRepository()

    def create_evaluacion(self, nombre, comienzo, ultima_actualizacion, peal_id):
        self.evaluaciones_repository.create_evaluacion(nombre, comienzo, ultima_actualizacion, peal_id)

    def get_evaluacion_by_id(self, evaluacion_id):
        return self.evaluaciones_repository.get_evaluacion_by_id(evaluacion_id)

    def update_evaluacion_by_id(self, evaluacion_id, nombre, comienzo, ultima_actualizacion, peal_id):
        self.evaluaciones_repository.update_evaluacion_by_id(evaluacion_id, nombre, comienzo, ultima_actualizacion, peal_id)

    def delete_evaluacion_by_id(self, evaluacion_id):
        self.evaluaciones_repository.delete_evaluacion_by_id(evaluacion_id)

    def get_evaluaciones_by_peal_id(self, peal_id):
        return self.evaluaciones_repository.get_evaluaciones_by_peal_id(peal_id)