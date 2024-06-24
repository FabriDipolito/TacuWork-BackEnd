from app.Repositories.encuesta_repository import EncuestaRepository

class EncuestaService:
    def __init__(self):
        self.encuesta_repository = EncuestaRepository()

    def create_encuesta(self, respuesta1, respuesta2, respuesta3, comentario, peal_id, nombre):
        encuesta = self.encuesta_repository.create_encuesta(respuesta1, respuesta2, respuesta3, comentario, peal_id, nombre)

        if encuesta is None:
            return None

        encuesta_object = {
            "id": encuesta[0],
            "respuesta1": encuesta[1],
            "respuesta2": encuesta[2],
            "respuesta3": encuesta[3],
            "comentario": encuesta[4],
            "peal_id": encuesta[5],
            "nombre": encuesta[6]
        }

        return encuesta_object

    def get_encuesta(self, encuesta_id):
        encuesta = self.encuesta_repository.get_encuesta(encuesta_id)
        if encuesta:
            encuesta_object = {
                "id": encuesta[0],
                "respuesta1": encuesta[1],
                "respuesta2": encuesta[2],
                "respuesta3": encuesta[3],
                "comentario": encuesta[4],
                "peal_id": encuesta[5]
            }
            return encuesta_object
        else:
            return None

    def delete_encuesta(self, encuesta_id):
        deleted_id = self.encuesta_repository.delete_encuesta(encuesta_id)
        return deleted_id

    def get_all_encuestas(self):
        encuestas = self.encuesta_repository.get_all_encuestas()
        encuestas_transformadas = []
        for encuesta in encuestas:
            encuesta_object = {
                "id": encuesta[0],
                "respuesta1": encuesta[1],
                "respuesta2": encuesta[2],
                "respuesta3": encuesta[3],
                "comentario": encuesta[4],
                "peal_id": encuesta[5],
                "nombre": encuesta[6]
            }
            encuestas_transformadas.append(encuesta_object)
        return encuestas_transformadas
