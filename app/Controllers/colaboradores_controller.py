from flask import request, jsonify
from app.Services.colaboradores_service import ColaboradoresService

class ColaboradoresController:
    def __init__(self):
        self.colaboradores_service = ColaboradoresService()

    def create_colaborador(self):
        data = request.get_json()
        nombre = data['nombre']
        apellido = data['apellido']
        edad = data['edad']
        hijos = data['hijos']
        zona_residencial = data['zona_residencial']
        telefono = data['telefono']
        nivel_educativo = data['nivel_educativo']
        egresos = data['egresos']
        peal_id = data['peal_id']
        self.colaboradores_service.create_colaborador(nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id)
        return jsonify({"message": "Colaborador creado exitosamente."}), 201

    def get_colaborador(self, colaborador_id):
        colaborador = self.colaboradores_service.get_colaborador_by_id(colaborador_id)
        if colaborador:
            return jsonify(colaborador), 200
        else:
            return jsonify({"message": "Colaborador no encontrado"}), 404

    def update_colaborador(self, colaborador_id):
        data = request.get_json()
        nombre = data['nombre']
        apellido = data['apellido']
        edad = data['edad']
        hijos = data['hijos']
        zona_residencial = data['zona_residencial']
        telefono = data['telefono']
        nivel_educativo = data['nivel_educativo']
        egresos = data['egresos']
        peal_id = data['peal_id']
        self.colaboradores_service.update_colaborador_by_id(colaborador_id, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id)
        return jsonify({"message": "Colaborador actualizado exitosamente."}), 200

    def delete_colaborador(self, colaborador_id):
        self.colaboradores_service.delete_colaborador_by_id(colaborador_id)
        return jsonify({"message": "Colaborador eliminado exitosamente."}), 200

    def get_all_colaboradores(self):
        colaboradores = self.colaboradores_service.get_all_colaboradores()
        return jsonify(colaboradores), 200

    def get_colaboradores_by_peal(self, peal_id):
        colaboradores = self.colaboradores_service.get_colaboradores_by_peal_id(peal_id)
        return jsonify(colaboradores), 200