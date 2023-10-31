from app.Repositories.colaboradores_repository import ColaboradoresRepository

class ColaboradoresService:
    def __init__(self):
        self.colaboradores_repository = ColaboradoresRepository()

    def create_colaborador(self, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id):
        self.colaboradores_repository.create_colaborador(nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id)

    def get_colaborador_by_id(self, colaborador_id):
        return self.colaboradores_repository.get_colaborador_by_id(colaborador_id)

    def update_colaborador_by_id(self, colaborador_id, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id):
        self.colaboradores_repository.update_colaborador_by_id(colaborador_id, nombre, apellido, edad, hijos, zona_residencial, telefono, nivel_educativo, egresos, peal_id)

    def delete_colaborador_by_id(self, colaborador_id):
        self.colaboradores_repository.delete_colaborador_by_id(colaborador_id)

    def get_all_colaboradores(self):
        return self.colaboradores_repository.get_all_colaboradores()

    def get_colaboradores_by_peal_id(self, peal_id):
        return self.colaboradores_repository.get_colaboradores_by_peal_id(peal_id)