from flask import Blueprint
from db import api
from .views import CreateAuthor, UpdateAuthor, DeleteAuthor

author_routes = Blueprint("author_routes", __name__)
api.add_resource(CreateAuthor, "/author/")
api.add_resource(UpdateAuthor, "/author/<int:author_id>/")
api.add_resource(DeleteAuthor, "/author/<int:author_id>/")