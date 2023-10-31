from app.Repositories.peal_repository import PealRepository

class PealService:
    def __init__(self):
        self.peal_repository = PealRepository()

    def create_peal(self, nombre, comienzo, fin):
        self.peal_repository.create_peal(nombre, comienzo, fin)

    def get_peal(self, peal_id):
        return self.peal_repository.get_peal(peal_id)

    def update_peal(self, peal_id, nombre, comienzo, fin):
        self.peal_repository.update_peal(peal_id, nombre, comienzo, fin)

    def delete_peal(self, peal_id):
        self.peal_repository.delete_peal(peal_id)

    def get_all_peals(self):
        return self.peal_repository.get_all_peals()