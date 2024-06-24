import base64

from app.Repositories.colaboradores_repository import ColaboradoresRepository

class ColaboradoresService:
    def __init__(self):
        self.colaboradores_repository = ColaboradoresRepository()

    def create_colaborador(self, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id, comienzo, finalizacion):
        col = self.colaboradores_repository.create_colaborador(nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id, comienzo, finalizacion)

        if col is None:
            return None

        colaborador_object = {
            "id": col[0],
            "nombre": col[1],
            "apellido": col[2],
            "edad": col[3],
            "hijos": col[4],
            "zona_residencial": col[5],
            "telefono": col[6],
            "nivel_educativo": col[7],
            "egresos": col[8],
            "peal_id": col[9],
            "comienzo": col[16]
        }

        return colaborador_object

    def get_colaborador_by_id(self, colaborador_id):
        return self.colaboradores_repository.get_colaborador_by_id(colaborador_id)

    def update_colaborador_by_id(self, colaborador_id, nombre, apellido, edad, hijos, zona_residencial, telefono,
                                 nivel_educativo, egresos, peal_id, banco=None, sucursal=None, numero_cuenta=None,
                                 nombre_emergencia=None, telefono_emergencia=None, imagen=None, comienzo=None, finalizacion=None):
        updated_colaborador = self.colaboradores_repository.update_colaborador_by_id(
            colaborador_id, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos,
            peal_id, banco, sucursal, numero_cuenta, nombre_emergencia, telefono_emergencia, imagen, comienzo, finalizacion
        )

        if updated_colaborador:
            return {
                "id": updated_colaborador[0],
                "nombre": updated_colaborador[1],
                "apellido": updated_colaborador[2],
                "edad": updated_colaborador[3],
                "hijos": updated_colaborador[4],
                "zona_residencial": updated_colaborador[5],
                "telefono": updated_colaborador[6],
                "nivel_educativo": updated_colaborador[7],
                "egresos": updated_colaborador[8],
                "peal_id": updated_colaborador[9],
                "imagen": base64.b64encode(updated_colaborador[10]).decode('utf-8') if updated_colaborador[10] else None,
                "banco": updated_colaborador[11],
                "sucursal": updated_colaborador[12],
                "numero_cuenta": updated_colaborador[13],
                "nombre_emergencia": updated_colaborador[14],
                "telefono_emergencia": updated_colaborador[15],
                "comienzo": updated_colaborador[16],
                "finalizacion": updated_colaborador[17]
            }
        else:
            return None

    def delete_colaborador_by_id(self, colaborador_id):
        self.colaboradores_repository.delete_colaborador_by_id(colaborador_id)

    def delete_colaboradores_by_ids(self, ids):
        return self.colaboradores_repository.delete_colaboradores_by_ids(ids)

    def get_all_colaboradores(self):
        colaboradores_arrays = self.colaboradores_repository.get_all_colaboradores()

        colaboradores_objects = [
            {
                "id": col[0],
                "nombre": col[1],
                "apellido": col[2],
                "edad": col[3],
                "hijos": col[4],
                "zona_residencial": col[5],
                "telefono": col[6],
                "nivel_educativo": col[7],
                "egresos": col[8],
                "peal_id": col[9],
                "imagen": base64.b64encode(col[10]).decode('utf-8') if col[10] else None,
                "banco": col[11],
                "sucursal": col[12],
                "numero_cuenta": col[13],
                "nombre_emergencia": col[14],
                "telefono_emergencia": col[15],
                "comienzo": col[16],
                "finalizacion": col[17]
            }
            for col in colaboradores_arrays
        ]

        return colaboradores_objects

    def get_colaboradores_by_peal_id(self, peal_id):
        return self.colaboradores_repository.get_colaboradores_by_peal_id(peal_id)