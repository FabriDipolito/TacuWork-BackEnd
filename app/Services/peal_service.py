from app.Repositories.peal_repository import PealRepository

class PealService:
    def __init__(self):
        self.peal_repository = PealRepository()

    def create_peal(self, nombre, comienzo, fin):
        peal = self.peal_repository.create_peal(nombre, comienzo, fin)

        if peal is None:
            return None

        peal_object = {
            "id": peal[0],
            "nombre": peal[1],
            "comienzo": peal[2],
            "fin": peal[3]
        }

        return peal_object

    def get_peal(self, peal_id):
        return self.peal_repository.get_peal(peal_id)

    def update_peal(self, peal_id, nombre, comienzo, fin):
        updated_peal = self.peal_repository.update_peal_by_id(peal_id, nombre, comienzo, fin)

        if updated_peal:
            return {
                "id": updated_peal[0],
                "nombre": updated_peal[1],
                "comienzo": updated_peal[2],
                "fin": updated_peal[3]
            }
        else:
            return None

    def delete_peal(self, peal_id):
        self.peal_repository.delete_peal(peal_id)

    def delete_peales_by_ids(self, ids):
        return self.peal_repository.delete_peales_by_ids(ids)

    def get_all_peals(self):
        peals = self.peal_repository.get_all_peals()

        peals_transformados = []

        for peal in peals:
            peal_transformado = {
                'id': peal[0],
                'nombre': peal[1],
                'comienzo': peal[2],
                'fin': peal[3]
            }

            peals_transformados.append(peal_transformado)

        return peals_transformados