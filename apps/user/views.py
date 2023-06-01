import datetime
import jwt
from flask import jsonify, request, current_app
from flask_restful import Resource
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash

from db import db
from .models import Users
from .schema import user_create_schema, login_schema, change_password, get_user
from .decorators import login_required



class CreateUser(Resource):
    """
    type = post;
    payload = {
                  "first_name": "acd",
                  "last_name": "xyz",
                  "email_id" : "abcd@gmail.com",
                  "password": "abcd123"
                }
    """
    def get(self):
        user_data = Users.query.all()
        return get_user.dump(user_data)

    def post(self):
        try:
            user_data = user_create_schema.load(request.get_json())
        except ValidationError as err:
            return {'error': err.messages}, 400
        user_data["password"] = generate_password_hash(user_data['password'])
        db.session.add(Users(**user_data))
        db.session.commit()
        return jsonify({'message': 'user added successfully'})
    


class Login(Resource):

    def post(self):
        # import pdb
        # pdb.set_trace()
        try:
            user_data = login_schema.load(request.get_json())
        except ValidationError as err:
            return {'error': err.messages}, 400
        user_id = Users.query.with_entities(Users.id_).filter(
            Users.email_id == user_data["email_id"].lower()
        ).scalar()  

        token = jwt.encode(
            {
                "user_id": user_id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            },
            current_app.config["SECRET_KEY"],
            algorithm="HS256",
        )
        result = {
            "token": token,
            "message": "logged in successfully....."
        }
        return result, 200


class ChangePassword(Resource):

    @login_required
    def post(self, args):
        try:
            user_data = change_password.load(request.get_json())
        except ValidationError as err:
            return {'error': err.messages}, 400

        user_id = jwt.decode(
                request.headers["Authorization"],
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"])["user_id"]

        user = Users.query.filter_by(id_=user_id).first()
        user.password = generate_password_hash(user_data['new_password'])
        db.session.commit()

        return jsonify({'message': 'password changed successfully'})