import bcrypt

from app.Repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return self.user_repository.create_user(username, hashed_password.decode('utf-8'))

    def validate_user(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return user
        return None
