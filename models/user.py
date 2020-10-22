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
from models.article import Article

class User(BaseModel, Base):
    """Representation of user"""
    __tablename__ = 'user'
    email = Column(String(128), primary_key=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    avatar = Column(String(500), nullable=False)
    token = Column(String(500), nullable=True)
    adress = Column(String(500), nullable=True)
    phone_number = Column(Integer, nullable=True)
    typ = Column(Integer, nullable=True, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def hashpwd(self, pwd):
        return generate_password_hash(pwd)


    def verify_password(self, pwd, hash):
        return check_password_hash(hash, pwd)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def as_dict_nopwd(self):
        a={c.name: getattr(self, c.name) for c in self.__table__.columns}
        a.pop('password', None)
        return a
'''
    def follower_list(self):
        """get follower list of a user"""
        follow_list_obj = models.storage.get_by_followed_id(Follow, self.id)
        follow_list = []
        for obj in follow_list_obj:
            follow_list.append(obj.follower_id)
        return follow_list

    def follow_list(self):
        """get list of user follow"""
        follow_list_obj = models.storage.get_by_follower_id(Follow, self.id)
        follow_list = []
        for obj in follow_list_obj:
            follow_list.append(obj.user_id)
        return follow_list

    def post_list(self):
        """get post list of a user"""
        post_list_obj = models.storage.getlist_by_attr(Post, self.id)
        post_list = []
        for obj in post_list:
            post_list.append(obj)
'''