from flask import jsonify, request, current_app
from flask_restful import Resource
from marshmallow import ValidationError

from db import db
from .models import Book, Category
from .schema import book_create_schema, category_create_schema, book_update_schema, category_update_schema, get_book, get_category, book_schema


class GetBook(Resource):
    def get(self):
        book_data = Book.query.options(db.joinedload(Book.category)).all()
        return book_schema.dump(book_data)


class CreateBook(Resource):
    """
    type = post;
    payload = {
                  "title": "book1",
                  "category_id_": 1,
                  "author_id_": 1
                }
    """
    def get(self):
        book_data = Book.query.all()
        return get_book.dump(book_data)
    
    def post(self):
        try:
            book_data = book_create_schema.load(request.get_json())
        except ValidationError as err:
            return {'error': err.messages}, 400
        db.session.add(Book(**book_data))
        db.session.commit()
        return jsonify({'message': 'book added successfully'})
    

class CreateCategory(Resource):
    """
    type = post;
    payload = {
                  "name":"cat1"
                }
    """
    def get(self):
        cat_data = Category.query.all()
        return get_category.dump(cat_data)

    def post(self):
        try:
            cat_data = category_create_schema.load(request.get_json())
        except ValidationError as err:
            return {'error': err.messages}, 400
        db.session.add(Category(**cat_data))
        db.session.commit()
        return jsonify({'message': 'category added successfully'})
    

class UpdateBook(Resource):
    def put(self, book_id):
        book = Book.query.filter_by(id_=book_id).first()
        if book:
            try:
                book_data = book_update_schema.load(request.get_json())
            except ValidationError as err:
                return {'error': err.messages}, 400
            book.title = book_data["title"]
            db.session.commit()
        else:
            return {"error": "not found"}, 404

        return jsonify({'message':'title changed successfully'})
    

class UpdateCategory(Resource):
    def put(self, category_id):
        category = Category.query.filter_by(id_=category_id).first()
        if category:
            try:
                cat_data = category_update_schema.load(request.get_json())
            except ValidationError as err:
                return {'error': err.messages}, 400
            category.name = cat_data["name"]
            db.session.commit()
        else:
            return {"error": "not found"}, 404

        return jsonify({'message':'name changed successfully'})
    
    
class DeleteBook(Resource):
    def delete(self, book_id):
        book = Book.query.filter_by(id_=book_id).first()
        if book:
            db.session.delete(book)
            db.session.commit()
        else:
            return {"error": "not found"}, 404

        return jsonify({'message':'book deleted successfully'})
    

class DeleteCategory(Resource):
    def delete(self, category_id):
        category = Category.query.filter_by(id_=category_id).first()
        if category:
            db.session.delete(category)
            db.session.commit()
        else:
            return {"error": "not found"}, 404
    
        return jsonify({'message':'category deleted successfully'})