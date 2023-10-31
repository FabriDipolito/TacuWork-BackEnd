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
        self.peal_service.create_peal(nombre, comienzo, fin)
        return jsonify({"message": "PEAL created successfully."}), 201

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
        self.peal_service.update_peal(peal_id, nombre, comienzo, fin)
        return jsonify({"message": "PEAL updated successfully."}), 200

    def delete_peal(self, peal_id):
        self.peal_service.delete_peal(peal_id)
        return jsonify({"message": "PEAL deleted successfully."}), 200

    def get_all_peals(self):
        peals = self.peal_service.get_all_peals()
        return jsonify(peals), 200