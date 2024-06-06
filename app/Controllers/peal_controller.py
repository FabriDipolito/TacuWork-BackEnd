from flask import request, jsonify
from app.Services.peal_service import PealService

class PealController:
    def __init__(self):
        self.peal_service = PealService()

    def create_peal(self):
        data = request.get_json()
        nombre = data['nombre']
        comienzo = data['comienzo']
        fin = data['fin']
        peal = self.peal_service.create_peal(nombre, comienzo, fin)
        if peal:
            return jsonify(peal), 201
        else:
            return jsonify({"message": "PEAL not created"}), 401

    def get_peal(self, peal_id):
        peal = self.peal_service.get_peal(peal_id)
        if peal:
            return jsonify(peal), 200
        else:
            return jsonify({"message": "PEAL not found"}), 404

    def update_peal(self, peal_id):
        data = request.get_json()
        nombre = data['nombre']
        comienzo = data['comienzo']
        fin = data['fin']
        peal = self.peal_service.update_peal(peal_id, nombre, comienzo, fin)
        if peal:
            return jsonify(peal), 201
        else:
            return jsonify({"message": "PEAL not updated"}), 401

    def delete_peal(self, peal_id):
        deleted_id = self.peal_service.delete_peal(peal_id)
        if deleted_id is not None:
            return jsonify({"message": "PEAL eliminado exitosamente.", "deleted_id": deleted_id}), 200
        else:
            return jsonify({"error": "Error al eliminar el PEAL."}), 500

    def delete_peales(self):
        try:
            ids = request.json.get('ids')
            if not ids:
                return jsonify({"error": "No IDs provided"}), 400

            deleted_ids = self.peal_service.delete_peales_by_ids(ids)
            return jsonify({"message": "PEALs eliminados exitosamente.", "deleted_ids": deleted_ids}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_all_peals(self):
        peals = self.peal_service.get_all_peals()
        return jsonify(peals), 200