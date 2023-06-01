from marshmallow import fields, Schema, validate, validates_schema, ValidationError
from sqlalchemy import func
from werkzeug.security import check_password_hash
import jwt
from flask import request, current_app

from .models import Users


class GetUser(Schema):
    class Meta:
        fields = ("id_", "first_name", "last_name", "email_id")

get_user = GetUser(many=True)

class CreateUser(Schema):
    first_name = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Please provide a First name."},
        validate=validate.Length(min=2)
    )
    last_name = fields.String(
        required=False, allow_none=True,
        validate=validate.Length(min=2)
    )
    email_id = fields.Email(
        allow_none=False, required=True,
        error_messages={"required": "Please provide an email address."},
    )
    password = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Please provide a valid password."},
        validate=validate.Length(min=5, max=20)
    )

    class Meta:
        fields = ("first_name", "last_name", "email_id", "password",)

    @validates_schema
    def validate_email(self, data, **kwargs):
        if Users.query.filter(func.lower(Users.email_id) == data.get("email")).first():
            errors = {"email": "please select different email address."}
            raise ValidationError(errors)

user_create_schema = CreateUser()


class LoginUser(Schema):
    email_id = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Please provide a email."}
    )
    password = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Please provide a password."},
    )

    class Meta:
        fields = ("email_id", "password",)

    @validates_schema
    def validate_user(self, data, **kwargs):
        user_obj = Users.query.filter(
            func.lower(Users.email_id) == data.get("email_id")
        ).first()
        if user_obj:
            if not check_password_hash(user_obj.password, data.get("password")):
                errors = {
                    "email": "login failed, please check email/ password and try again."
                }
                raise ValidationError(errors)
        else:
            errors = {
                "email": "login failed, please check email/ password and try again."
            }
            raise ValidationError(errors)
        
login_schema = LoginUser()


class ChangePassword(Schema):
    old_password = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Please provide old password."}
    )
    new_password = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Please provide new password."},
        validate=validate.Length(min=5, max=20)
    )

    class Meta:
        fields = ("old_password", "new_password",)

    @validates_schema
    def validate_password(self, data, **kwargs):
        user_id = jwt.decode(
                request.headers["Authorization"],
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"])["user_id"]
    
        user = Users.query.filter_by(id_=user_id).first()
        if not check_password_hash(user.password, data.get("old_password")):
            errors = {
                "password": "failed, enter correct old_password."
            }
            raise ValidationError(errors)

change_password = ChangePassword()