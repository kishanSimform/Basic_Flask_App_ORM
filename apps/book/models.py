from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import db
from apps.author.models import Author


class Category(db.Model):
    __tablename__ = "categories"
    id_ = Column(Integer(), primary_key=True, index=True)
    name = Column(String(100), nullable=True)
    books = relationship('Book', backref='category')


class Book(db.Model):
    __tablename__ = "books"
    id_ = Column(Integer(), primary_key=True, index=True)
    title = Column(String(100), nullable=True)
    author_id_ = Column(Integer(), ForeignKey(Author.id_, ondelete='CASCADE') ,nullable=False)
    category_id_ = Column(Integer(), ForeignKey(Category.id_, ondelete='CASCADE') ,nullable=False)
