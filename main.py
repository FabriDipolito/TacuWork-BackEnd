from flask import Flask

from app.Controllers.colaboradores_controller import ColaboradoresController
from app.Controllers.peal_controller import PealController
from app.Controllers.evaluaciones_controller import EvaluacionesController

app = Flask(__name__)

peal_controller = PealController()
colaboradores_controller = ColaboradoresController()
evaluaciones_controller = EvaluacionesController()


@app.route("/peal", methods=['POST'])
def create_peal():
    return peal_controller.create_peal()


@app.route("/peal/<int:peal_id>", methods=['GET'])
def get_peal(peal_id):
    return peal_controller.get_peal(peal_id)


@app.route("/peal/<int:peal_id>", methods=['PUT'])
def update_peal(peal_id):
    return peal_controller.update_peal(peal_id)


@app.route("/peal/<int:peal_id>", methods=['DELETE'])
def delete_peal(peal_id):
    return peal_controller.delete_peal(peal_id)


@app.route("/peal", methods=['GET'])
def get_all_peals():
    return peal_controller.get_all_peals()


# Rutas para las operaciones de COLABORADORES
@app.route("/colaboradores", methods=['POST'])
def create_colaborador():
    return colaboradores_controller.create_colaborador()


@app.route("/colaboradores/<int:colaborador_id>", methods=['GET'])
def get_colaborador(colaborador_id):
    return colaboradores_controller.get_colaborador(colaborador_id)


@app.route("/colaboradores/<int:colaborador_id>", methods=['PUT'])
def update_colaborador(colaborador_id):
    return colaboradores_controller.update_colaborador(colaborador_id)


@app.route("/colaboradores/<int:colaborador_id>", methods=['DELETE'])
def delete_colaborador(colaborador_id):
    return colaboradores_controller.delete_colaborador(colaborador_id)


@app.route("/colaboradores", methods=['GET'])
def get_all_colaboradores():
    return colaboradores_controller.get_all_colaboradores()


@app.route("/colaboradores/peal/<int:peal_id>", methods=['GET'])
def get_colaboradores_by_peal(peal_id):
    return colaboradores_controller.get_colaboradores_by_peal(peal_id)


# Rutas para las operaciones de EVALUACIONES
@app.route("/evaluaciones", methods=['POST'])
def create_evaluacion():
    return evaluaciones_controller.create_evaluacion()


@app.route("/evaluaciones/<int:evaluacion_id>", methods=['GET'])
def get_evaluacion(evaluacion_id):
    return evaluaciones_controller.get_evaluacion(evaluacion_id)


@app.route("/evaluaciones/<int:evaluacion_id>", methods=['PUT'])
def update_evaluacion(evaluacion_id):
    return evaluaciones_controller.update_evaluacion(evaluacion_id)


@app.route("/evaluaciones/<int:evaluacion_id>", methods=['DELETE'])
def delete_evaluacion(evaluacion_id):
    return evaluaciones_controller.delete_evaluacion(evaluacion_id)


@app.route("/evaluaciones", methods=['GET'])
def get_all_evaluaciones():
    return evaluaciones_controller.get_all_evaluaciones()


@app.route("/evaluaciones/peal/<int:peal_id>", methods=['GET'])
def get_evaluaciones_by_peal(peal_id):
    return evaluaciones_controller.get_evaluaciones_by_peal(peal_id)


if __name__ == '__main__':
    app.run()
