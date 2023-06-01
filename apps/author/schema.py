from marshmallow import fields, Schema, validate, validates_schema, ValidationError
from marshmallow_enum import EnumField
from sqlalchemy import func
from .models import Gender

from .models import Author


class GetAuthor(Schema):
    gender = EnumField(Gender)

    class Meta:
        fields = ("id_", "name", "email_id", "address", "gender", )

get_author = GetAuthor(many=True)


class CreateAuthor(Schema):
    name = fields.String(
        required=True, allow_none=False, default=None,
        error_messages={"required": "Please provide a name."},
        validate=validate.Length(min=2)
    )
    email_id = fields.Email(
        required=True, allow_none=False, default=None,
        error_messages={"required": "Please provide a email."},
    )
    address = fields.String(
        required=True, allow_none=False, default=None,
        error_messages={"required": "Please provide a address."},
    )
    gender = EnumField(Gender,
        required=True, allow_none=False, default=None,
        error_messages={"required": "Please provide a gender"},
    )

    class Meta:
        fields = ("name", "email_id", "address", "gender",)

    @validates_schema
    def validate_email(self, data, **kwargs):
        if Author.query.filter(func.lower(Author.email_id) == data.get("email_id")).first():
            errors = {"email": "please select different email address."}
            raise ValidationError(errors)
        
author_create_schema = CreateAuthor()


class UpdateAuthor(Schema):
    name = fields.String(
        required=False, allow_none=True,
        validate=validate.Length(min=2)
    )
    email_id = fields.Email(
        required=False, allow_none=True,
    )
    address = fields.String(
        required=False, allow_none=True,
    )
    gender = EnumField(Gender,
        required=False, allow_none=True,
    )

    class Meta:
        fields = ("name", "email_id", "address", "gender",)

    @validates_schema
    def validate_email(self, data, **kwargs):
        if Author.query.filter(func.lower(Author.email_id) == data.get("email_id")).first():
            errors = {"email": "please select different email address."}
            raise ValidationError(errors)
        
author_update_schema = UpdateAuthor()