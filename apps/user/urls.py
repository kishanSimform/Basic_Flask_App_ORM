from flask import Blueprint

from db import api
from .views import CreateUser, Login, ChangePassword

user_routes = Blueprint("user_routes", __name__)
api.add_resource(CreateUser, "/users/")
api.add_resource(Login, "/login/")
api.add_resource(ChangePassword, "/change_password/")