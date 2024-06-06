from flask import Flask, request, make_response

from flask_cors import CORS

from app.Controllers.user_controller import UserController
from app.Controllers.colaboradores_controller import ColaboradoresController
from app.Controllers.peal_controller import PealController
from app.Controllers.evaluaciones_controller import EvaluacionesController
from app.Controllers.puntajes_controller import PuntajesController

app = Flask(__name__)

CORS(app)

peal_controller = PealController()
colaboradores_controller = ColaboradoresController()
evaluaciones_controller = EvaluacionesController()
puntajes_controller = PuntajesController()
user_controller = UserController()


@app.route("/peal", methods=['OPTIONS', 'POST', 'GET', 'DELETE'])
def create_peal():
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'POST':
        return peal_controller.create_peal()
    elif request.method == 'GET':
        return peal_controller.get_all_peals()
    elif request.method == 'DELETE':
        return peal_controller.delete_peales()


@app.route("/peal/<int:peal_id>", methods=['OPTIONS', 'PUT', 'DELETE', 'GET'])
def get_peal(peal_id):
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'PUT':
        return peal_controller.update_peal(peal_id)
    elif request.method == 'GET':
        return peal_controller.get_peal(peal_id)
    elif request.method == 'DELETE':
        return peal_controller.delete_peal(peal_id)

# Rutas para las operaciones de COLABORADORES
@app.route("/colaboradores", methods=['OPTIONS', 'POST', 'GET', 'DELETE'])
def create_colaborador():
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'POST':
        return colaboradores_controller.create_colaborador()
    elif request.method == 'GET':
        return colaboradores_controller.get_all_colaboradores()
    elif request.method == 'DELETE':
        return colaboradores_controller.delete_colaboradores()


@app.route("/colaboradores/<int:colaborador_id>", methods=['OPTIONS', 'GET', 'PUT', 'DELETE'])
def get_colaborador(colaborador_id):
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'GET':
        return colaboradores_controller.get_colaborador(colaborador_id)
    elif request.method == 'PUT':
        return colaboradores_controller.update_colaborador(colaborador_id)
    elif request.method == 'DELETE':
        return colaboradores_controller.delete_colaborador(colaborador_id)

@app.route("/colaboradores/peal/<int:peal_id>", methods=['GET'])
def get_colaboradores_by_peal(peal_id):
    return colaboradores_controller.get_colaboradores_by_peal(peal_id)


# Rutas para las operaciones de EVALUACIONES

@app.route("/evaluaciones", methods=['OPTIONS', 'POST', 'GET', 'DELETE'])
def create_evaluacion():
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'POST':
        return evaluaciones_controller.create_evaluacion()
    elif request.method == 'GET':
        return evaluaciones_controller.get_all_evaluaciones()
    elif request.method == 'DELETE':
        return evaluaciones_controller.delete_evaluaciones()


@app.route("/evaluaciones/<int:evaluacion_id>", methods=['OPTIONS', 'GET', 'PUT', 'DELETE'])
def get_evaluacion(evaluacion_id):
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'GET':
        return evaluaciones_controller.get_evaluacion(evaluacion_id)
    elif request.method == 'PUT':
        return evaluaciones_controller.update_evaluacion(evaluacion_id)
    elif request.method == 'DELETE':
        return evaluaciones_controller.delete_evaluacion(evaluacion_id)

@app.route("/evaluaciones/peal/<int:peal_id>", methods=['OPTIONS', 'GET'])
def get_evaluaciones_by_peal(peal_id):
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'GET':
        return evaluaciones_controller.get_evaluaciones_by_peal(peal_id)

# Rutas para las operaciones de PUNTAJES
@app.route("/puntajes", methods=['OPTIONS', 'POST', 'GET', 'DELETE'])
def create_puntaje():
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'POST':
        return puntajes_controller.create_puntaje()
    elif request.method == 'GET':
        return puntajes_controller.get_all_puntajes()
    elif request.method == 'DELETE':
        return puntajes_controller.delete_puntajes()

@app.route("/puntajes/<int:colaborador_id>/<int:evaluacion_id>", methods=['GET', 'PUT', 'DELETE'])
def get_puntaje(colaborador_id, evaluacion_id):
    if request.method == 'OPTIONS':
        return build_preflight_response()
    elif request.method == 'GET':
        return puntajes_controller.get_puntaje(colaborador_id, evaluacion_id)
    elif request.method == 'PUT':
        return puntajes_controller.update_puntaje(colaborador_id, evaluacion_id)
    elif request.method == 'DELETE':
        return puntajes_controller.delete_puntaje(colaborador_id, evaluacion_id)

# Ruta para operacion de Authenticar

@app.route('/api/users', methods=['POST'])
def create_user():
    return user_controller.create_user()

@app.route('/api/auth/login', methods=['POST'])
def authenticate():
    return user_controller.authenticate()

def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run()
