from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from db import db
from .models import Author
from .schema import author_create_schema, author_update_schema, get_author



class CreateAuthor(Resource):
    """
    type = post;
    payload = {
                  "name": "acd",
                  "email_id" : "abcd@gmail.com",
                  "address": "india",
                  "gender": "M",
                  "is_active": "False"
                }
    """
    def get(self):
        author = Author.query.all()
        if author:
            result = get_author.dump(author)
            return result
        else:
            return {"error": "not found"}, 404
        

    def post(self):
        try:
            author_data = author_create_schema.load(request.get_json())
        except ValidationError as err:
            return {'error': err.messages}, 400
        db.session.add(Author(**author_data))
        db.session.commit()
        return jsonify({'message': 'author added successfully'})
    

class UpdateAuthor(Resource):
    def put(self, author_id):
        author = Author.query.filter_by(id_=author_id).first()
        if author:
            try:
                author_data = author_update_schema.load(request.get_json())
            except ValidationError as err:
                return {'error': err.messages}, 400

            author.name = author_data["name"] if "name" in author_data  else author.name
            author.email_id = author_data["email_id"] if "email_id" in author_data else author.email_id
            author.address = author_data["address"] if "address" in author_data  else author.address
            author.gender = author_data["gender"] if "gender" in author_data  else author.gender
            db.session.commit()
        else:
            return {"error": "not found"}, 404

        return jsonify({'message':'author details changed successfully'})
    

class DeleteAuthor(Resource):
    def delete(self, author_id):
        author = Author.query.filter_by(id_=author_id).first()
        if author:
            db.session.delete(author)
            db.session.commit()
        else:
            return {"error": "not found"}, 404
    
        return jsonify({'message':'author deleted successfully'})
    

