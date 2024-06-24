from flask import request, jsonify
from app.Services.encuesta_service import EncuestaService

class EncuestaController:
    def __init__(self):
        self.encuesta_service = EncuestaService()

    def create_encuesta(self):
        data = request.get_json()
        respuesta1 = data['respuesta1']
        respuesta2 = data['respuesta2']
        respuesta3 = data['respuesta3']
        comentario = data.get('comentario', '')
        peal_id = data['peal_id']
        nombre = data.get('nombre', None)
        encuesta = self.encuesta_service.create_encuesta(respuesta1, respuesta2, respuesta3, comentario, peal_id, nombre)
        if encuesta:
            return jsonify(encuesta), 201
        else:
            return jsonify({"message": "Encuesta not created"}), 401

    def get_encuesta(self, encuesta_id):
        encuesta = self.encuesta_service.get_encuesta(encuesta_id)
        if encuesta:
            return jsonify(encuesta), 200
        else:
            return jsonify({"message": "Encuesta not found"}), 404

    def delete_encuesta(self, encuesta_id):
        deleted_id = self.encuesta_service.delete_encuesta(encuesta_id)
        if deleted_id is not None:
            return jsonify({"message": "Encuesta eliminada exitosamente.", "deleted_id": deleted_id}), 200
        else:
            return jsonify({"error": "Error al eliminar la Encuesta."}), 500

    def get_all_encuestas(self):
        encuestas = self.encuesta_service.get_all_encuestas()
        return jsonify(encuestas), 200