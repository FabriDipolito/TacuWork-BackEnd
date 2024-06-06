from flask import request, jsonify

from app.Services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def create_user(self):
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user = self.user_service.create_user(username, password)
        if user:
            return jsonify(user), 201
        else:
            return jsonify({"message": "User could not be created"}), 400

    def authenticate(self):
        data = request.json
        username = data.get('username')
        password = data.get('password')
        user = self.user_service.validate_user(username, password)
        if user:
            return jsonify(user)
        else:
            return jsonify({"message": "Invalid credentials"}), 401
