from sqlalchemy import Column, Integer, String, Text, Boolean, Enum
import enum 
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship
from db import db


class Gender(enum.Enum):
    M = "Male"
    F = "Female"
    O = "Other"
    

class Author(db.Model):
    __tablename__ = "authors"
    id_ = Column(Integer(), primary_key=True, index=True)
    name = Column(String(100), nullable=True)
    email_id = Column(EmailType)
    address = Column(Text())
    gender = Column(Enum(Gender))
    is_active = Column(Boolean, default=False, nullable=False)
    books = relationship('Book', backref='author')
    