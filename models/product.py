#!/usr/bin/python3
"""
Creat table product in db
"""

import models
from models.Model_Com import BaseModel, Base, DateTime
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from datetime import datetime
from sqlalchemy.orm import relationship
from models.likes import Likes

class Products(BaseModel, Base):
    """Representation of product"""
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    tag_id = Column(String(60), ForeignKey('tags.id'), nullable=False)
    category_id = Column(String(60), ForeignKey('category.id'), nullable=False)
    title = Column(String(20), nullable=False)
    description = Column(String(2000), nullable=True)
    prix = Column(Integer, nullable=False)
    version = Column(String(20), nullable=True)
    promoted = Column(Integer, nullable=True)

    def productlist(self):
        """
            product list
        """
        lt = []
        for i in models.storage.all(Article).values():
            if i.post_id == self.id:
                lt.append(i)
        return lt

    def reaction_list_source_user_id(self):
        """
            list reaction of product
        """
        rect_list = self.reactionlist()
        source_list = []
        for react in rect_list:
            source_list.append(react.source_user_id)
        return source_list

    def number_of_reaction(self):
        """get the number of reaction of a prodcut"""
        react_list = self.reactionlist()
        num_of_react = len(react_list)
        return (str(num_of_react))


    def __init__(self, *args, **kwargs):
        """initializes product"""
        super().__init__(*args, **kwargs)