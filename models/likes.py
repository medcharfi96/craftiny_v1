#!/usr/bin/python3
"""
Creat table like in db
"""

import models
from models.Model_Com import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Likes(BaseModel, Base):
    """Representation of likes"""
    __tablename__ = 'likes'
    __table_args__ = {'extend_existing': True}
    article_id = Column(String(60), ForeignKey('article.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes like"""
        super().__init__(*args, **kwargs)
