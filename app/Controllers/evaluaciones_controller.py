from flask import request, jsonify
from app.Services.evaluaciones_service import EvaluacionesService

class EvaluacionesController:
    def __init__(self):
        self.evaluaciones_service = EvaluacionesService()

    def create_evaluacion(self):
        data = request.get_json()
        nombre = data['nombre']
        comienzo = data['comienzo']
        ultima_actualizacion = data['ultima_actualizacion']
        peal_id = data['peal_id']
        evaluacion = self.evaluaciones_service.create_evaluacion(nombre, comienzo, ultima_actualizacion, peal_id)
        if evaluacion:
            return jsonify(evaluacion), 201
        else:
            return jsonify({"message": "Evaluación no creada"}), 401

    def get_evaluacion(self, evaluacion_id):
        evaluacion = self.evaluaciones_service.get_evaluacion_by_id(evaluacion_id)
        if evaluacion:
            return jsonify(evaluacion), 200
        else:
            return jsonify({"message": "Evaluación no encontrada"}), 404

    def update_evaluacion(self, evaluacion_id):
        data = request.get_json()
        nombre = data['nombre']
        comienzo = data['comienzo']
        ultima_actualizacion = data['ultima_actualizacion']
        peal_id = data['peal_id']
        evaluacion = self.evaluaciones_service.update_evaluacion_by_id(evaluacion_id, nombre, comienzo, ultima_actualizacion, peal_id)
        if evaluacion:
            return jsonify(evaluacion), 201
        else:
            return jsonify({"message": "Evaluación no creada"}), 401

    def delete_evaluacion(self, evaluacion_id):
        deleted_id = self.evaluaciones_service.delete_evaluacion_by_id(evaluacion_id)
        if deleted_id is not None:
            return jsonify({"message": "Evaluación eliminada exitosamente.", "deleted_id": deleted_id}), 200
        else:
            return jsonify({"error": "Error al eliminar la evaluación."}), 500

    def delete_evaluaciones(self):
        try:
            ids = request.json.get('ids')
            if not ids:
                return jsonify({"error": "No IDs provided"}), 400

            deleted_ids = self.evaluaciones_service.delete_evaluaciones_by_ids(ids)
            return jsonify({"message": "Evaluaciones eliminadas exitosamente.", "deleted_ids": deleted_ids}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_all_evaluaciones(self):
        evaluaciones = self.evaluaciones_service.get_all_evaluaciones()
        return jsonify(evaluaciones), 200

    def get_evaluaciones_by_peal(self, peal_id):
        evaluaciones = self.evaluaciones_service.get_evaluaciones_by_peal_id(peal_id)
        return jsonify(evaluaciones), 200