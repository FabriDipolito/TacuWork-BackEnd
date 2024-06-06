from flask import jsonify, request
from app.Services.puntajes_service import PuntajesService

class PuntajesController:
    def __init__(self):
        self.puntajes_service = PuntajesService()

    def create_puntaje(self):
        data = request.get_json()

        # Extraer datos del JSON (adaptar según tus necesidades)
        colaborador_id = data.get('colaborador_id')
        evaluacion_id = data.get('evaluacion_id')
        adaptacion_al_cambio = data.get('adaptacion_al_cambio')
        habilidades_relacionales = data.get('habilidades_relacionales')
        comunicacion = data.get('comunicacion')
        liderazgo = data.get('liderazgo')
        proactividad = data.get('proactividad')
        presencia = data.get('presencia')
        puntualidad = data.get('puntualidad')
        porcentaje_asistencia = data.get('porcentaje_asistencia')
        trabajo_en_equipo = data.get('trabajo_en_equipo')
        responsabilidades = data.get('responsabilidades')
        rendimiento_laboral = data.get('rendimiento_laboral')

        # Llamada a la función del servicio
        puntaje = self.puntajes_service.create_puntaje(
            colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
            comunicacion, liderazgo, proactividad, presencia, puntualidad,
            porcentaje_asistencia, trabajo_en_equipo, responsabilidades, rendimiento_laboral
        )

        if puntaje:
            return jsonify(puntaje), 200
        else:
            return jsonify({"message": "Puntaje no encontrado"}), 404

    def get_puntaje(self, colaborador_id, evaluacion_id):
        puntaje = self.puntajes_service.get_puntaje(colaborador_id, evaluacion_id)
        if puntaje:
            return jsonify(puntaje), 200
        else:
            return jsonify({"message": "Puntaje no encontrado"}), 404

    def update_puntaje(self, colaborador_id, evaluacion_id):
        data = request.get_json()
        adaptacion_al_cambio = data.get('adaptacion_al_cambio')
        habilidades_relacionales = data.get('habilidades_relacionales')
        comunicacion = data.get('comunicacion')
        liderazgo = data.get('liderazgo')
        proactividad = data.get('proactividad')
        presencia = data.get('presencia')
        puntualidad = data.get('puntualidad')
        porcentaje_asistencia = data.get('porcentaje_asistencia')
        trabajo_en_equipo = data.get('trabajo_en_equipo')
        responsabilidades = data.get('responsabilidades')
        rendimiento_laboral = data.get('rendimiento_laboral')

        puntaje = self.puntajes_service.update_puntaje(colaborador_id, evaluacion_id, adaptacion_al_cambio, habilidades_relacionales,
                                              comunicacion, liderazgo, proactividad, presencia, puntualidad,
                                              porcentaje_asistencia, trabajo_en_equipo, responsabilidades,
                                              rendimiento_laboral)
        if puntaje:
            return jsonify(puntaje), 200
        else:
            return jsonify({"message": "Puntaje no actualizado"}), 404

    def delete_puntaje(self, colaborador_id, evaluacion_id):
        self.puntajes_service.delete_puntaje(colaborador_id, evaluacion_id)
        return jsonify({"message": "Puntaje eliminado exitosamente."}), 200

    def delete_puntajes(self):
        try:
            data = request.get_json()
            colaborador_ids = data.get('colaborador_ids')
            evaluacion_ids = data.get('evaluacion_ids')

            if not colaborador_ids or not evaluacion_ids:
                return jsonify({"error": "colaborador_ids y evaluacion_ids son necesarios"}), 400

            if len(colaborador_ids) != len(evaluacion_ids):
                return jsonify({"error": "colaborador_ids y evaluacion_ids deben tener la misma longitud"}), 400

            deleted_records = self.puntajes_service.delete_puntajes_by_ids(colaborador_ids, evaluacion_ids)
            return jsonify({"message": "Puntajes eliminados exitosamente.", "deleted_records": deleted_records}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_all_puntajes(self):
        puntajes = self.puntajes_service.get_all_puntajes()
        return jsonify(puntajes), 200
