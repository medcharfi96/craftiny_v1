#!/usr/bin/python3
"""
Creat table Post in db
"""

import models
from models.Model_Com import BaseModel, Base, DateTime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from datetime import datetime
from sqlalchemy.orm import relationship
from models.likes import Likes
from models.category import Category

class Article(BaseModel, Base):
    """Representation of article"""
    __tablename__ = 'article'
    __table_args__ = {'extend_existing': True}
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    tag_id = Column(String(60), ForeignKey('tags.id'), nullable=False)
    category_id = Column(String(60), ForeignKey('category.id'), nullable=False)
    date_article = Column(DateTime, nullable=True, default=datetime.utcnow)
    title = Column(String(20), nullable=False)
    description = Column(String(2000), nullable=True)
    content = Column(String(20), nullable=False)
    version = Column(String(20), nullable=True)
    promoted = Column(Integer, nullable=True)
    comment_id = relationship("Comment",
                              backref="comment",
                              cascade="all, delete, delete-orphan")
    like_id = relationship("Likes",
                              backref="likes",
                              cascade="all, delete, delete-orphan")

    def articalelist(self):
        """
            reacts list
        """
        lt = []
        for i in models.storage.all(Article).values():
            if i.post_id == self.id:
                lt.append(i)
        return lt

    def reaction_list_source_user_id(self):
        """
            user who reacted this post
        """
        rect_list = self.reactionlist()
        source_list = []
        for react in rect_list:
            source_list.append(react.source_user_id)
        return source_list

    def number_of_reaction(self):
        """get the number of reaction of a post"""
        react_list = self.reactionlist()
        num_of_react = len(react_list)
        return (str(num_of_react))

    def check_if_user_reacted(self, follower_id):
        """
        check if a user is already react on a post
        """
        reactor_list = self.reaction_list_source_user_id()
        for id in reactor_list:
            if id == follower_id:
                return True
        return False


    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)