#!/usr/bin/python3
"""
Creat table User in db
"""

from datetime import datetime
import models
from models.Model_Com import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from models.likes import Likes

class User(BaseModel, Base):
    """Representation of user"""
    __tablename__ = 'user'
    email = Column(String(128), primary_key=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=True)
    avatar = Column(String(500), nullable=True)
    token = Column(String(500), nullable=True)
    adress = Column(String(500), nullable=True)
    phone_number = Column(Integer, nullable=False)
    typ = Column(Integer, nullable=True, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    product_id = relationship("Products",
                              backref="product",
                              cascade="all, delete, delete-orphan")
    article_id = relationship("Article",
                              backref="article",
                              cascade="all, delete, delete-orphan")
    comments_id = relationship("Comment",
                              backref="comment",
                              cascade="all, delete, delete-orphan")
    like_id = relationship("Likes",
                              backref="likes",
                              cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def hashpwd(self, pwd):
		""" hash coding password"""
        return generate_password_hash(pwd)


    def verify_password(self, pwd, hash):
		""" password verification"""
        return check_password_hash(hash, pwd)

    def as_dict(self):
		""" to disct without password"""
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def as_dict_nopwd(self):
		""" to disct without password"""
        a={c.name: getattr(self, c.name) for c in self.__table__.columns}
        a.pop('password', None)
        return a


    def post_list(self):
        """get post list of a user"""
        post_list_obj = models.storage.getlist_by_attr(Post, self.id)
        post_list = []
        for obj in post_list:
            post_list.append(obj)
