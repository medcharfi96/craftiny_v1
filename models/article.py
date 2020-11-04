#!/usr/bin/python3
"""
class article
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
        article list
        """
        lt = []
        for i in models.storage.all(Article).values():
            if i.post_id == self.id:
                lt.append(i)
        return lt

    def number_of_reaction(self):
        """get the number of reaction of a article"""
        react_list = self.reactionlist()
        num_of_react = len(react_list)
        return (str(num_of_react))


    def __init__(self, *args, **kwargs):
        """initializes article"""
        super().__init__(*args, **kwargs)