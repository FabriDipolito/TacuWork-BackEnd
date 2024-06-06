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
        colaborador = self.colaboradores_service.create_colaborador(nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id)
        if colaborador:
            return jsonify(colaborador), 201
        else:
            return jsonify({"message": "Colaborador no se pudo crear"}),

    def get_colaborador(self, colaborador_id):
        colaborador = self.colaboradores_service.get_colaborador_by_id(colaborador_id)
        if colaborador:
            return jsonify(colaborador), 200
        else:
            return jsonify({"message": "Colaborador no encontrado"}), 404

    def update_colaborador(self, colaborador_id):
        data = request.form
        imagen = request.files.get('imagen')
        colaborador = self.colaboradores_service.update_colaborador_by_id(
            colaborador_id,
            data.get('nombre'),
            data.get('apellido'),
            int(data.get('edad')),
            int(data.get('hijos')),
            data.get('zona_residencial'),
            data.get('telefono'),
            data.get('nivel_educativo'),
            data.get('egresos'),
            int(data.get('peal_id')),
            data.get('banco'),
            data.get('sucursal'),
            data.get('numero_cuenta'),
            data.get('nombre_emergencia'),
            data.get('telefono_emergencia'),
            imagen
        )
        if colaborador:
            return jsonify(colaborador), 201
        else:
            return jsonify({"error": "No se pudo actualizar el colaborador"}), 400

    def delete_colaborador(self, colaborador_id):
        self.colaboradores_service.delete_colaborador_by_id(colaborador_id)
        return jsonify({"message": "Colaborador eliminado exitosamente."}), 200

    def delete_colaboradores(self):
        try:
            ids = request.json.get('ids')
            if not ids:
                return jsonify({"error": "No IDs provided"}), 400

            deleted_ids = self.colaboradores_service.delete_colaboradores_by_ids(ids)
            return jsonify({"message": "Colaboradores eliminados exitosamente.", "deleted_ids": deleted_ids}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_all_colaboradores(self):
        colaboradores = self.colaboradores_service.get_all_colaboradores()
        return jsonify(colaboradores), 200

    def get_colaboradores_by_peal(self, peal_id):
        colaboradores = self.colaboradores_service.get_colaboradores_by_peal_id(peal_id)
        return jsonify(colaboradores), 200