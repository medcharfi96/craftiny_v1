#!/usr/bin/python3
"""
Creat table reaction in db
"""

import models
from models.Model_Com import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class Comment(BaseModel, Base):
    """Representation of comment"""
    __tablename__ = 'comment'
    __table_args__ = {'extend_existing': True}
    article_id = Column(String(60), ForeignKey('article.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    content = Column(String(200), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
