from sqlalchemy import Column, Integer, String, Text, Boolean, Enum
from sqlalchemy_utils import EmailType
from db import db


class Users(db.Model):
    __tablename__ = "users"
    id_ = Column(Integer(), primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)
    email_id = Column(EmailType, nullable=False, unique=True)
    password = Column(Text, nullable=False)