from flask import Blueprint
from db import api
from .views import CreateBook, CreateCategory, UpdateBook, UpdateCategory, DeleteBook, DeleteCategory, GetBook


book_routes = Blueprint("book_routes", __name__)
api.add_resource(CreateBook, "/book/")
api.add_resource(UpdateBook, "/book/<int:book_id>/")
api.add_resource(DeleteBook, "/book/<int:book_id>/")
api.add_resource(GetBook, "/book/all/")


category_routes = Blueprint("category_routes", __name__)
api.add_resource(CreateCategory, "/category/")
api.add_resource(UpdateCategory, "/category/<int:category_id>/")
api.add_resource(DeleteCategory, "/category/<int:category_id>/")
