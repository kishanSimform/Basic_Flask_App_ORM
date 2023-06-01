from marshmallow import fields, Schema
from sqlalchemy import func
from apps.author.schema import GetAuthor


class GetBook(Schema):
    class Meta:
        fields = ("id_", "title",)

get_book = GetBook(many=True)


class GetCategory(Schema):
    class Meta:
        fields = ("id_", "name",)

get_category = GetCategory(many=True)


class CreateBook(Schema):
    title = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Please provide a name."}
    )
    category_id_ = fields.Integer(
        required=True, allow_none=False,
        error_messages={"required": "Please provide a valid category."}
    )
    author_id_ = fields.Integer(
        required=True, allow_none=False,
        error_messages={"required": "Please provide a valid author."}
    )
    
    class Meta:
        fields = ("title", "category_id_", "author_id_",)

        
book_create_schema = CreateBook()


class CreateCategory(Schema):
    name = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Please provide a name."}
    )

    class Meta:
        fields = ("name",)

category_create_schema = CreateCategory()


class UpdateBook(Schema):
    title = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Provide new title name."}
    )

    class Meta:
        fields = ("title",)

book_update_schema = UpdateBook()


class UpdateCategory(Schema):
    name = fields.String(
        required=True, allow_none=False,
        error_messages={"required": "Provide new name."}
    )

    class Meta:
        fields = ("name",)

category_update_schema = UpdateCategory()



class BookSchema(Schema):
    category = fields.Nested(GetCategory())
    author = fields.Nested(GetAuthor())
 
    class Meta:
        fields = ("id_", "title", "category", "author")

book_schema = BookSchema(many=True)