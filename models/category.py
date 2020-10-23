#!/usr/bin/python3
"""

"""

import models
from models.Model_Com import BaseModel, Base, DateTime
import sqlalchemy
from sqlalchemy import Column, String
from datetime import datetime
from sqlalchemy.orm import relationship
from models.product import Products

class Category(Base, BaseModel):
	"""Representation of category"""
	__tablename__ = 'category'
	__table_args__ = {'extend_existing': True}
	label = Column(String(20), nullable=True)
	product_id = relationship("Products",
							   backref="get",
							   cascade="all, delete, delete-orphan")
	article_id = relationship("Article",
							   backref="post",
							   cascade="all, delete, delete-orphan")

	def __init__(self, *args, **kwargs):
		"""initializes user"""
		super().__init__(*args, **kwargs)
