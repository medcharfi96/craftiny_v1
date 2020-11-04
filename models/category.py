#!/usr/bin/python3
"""
category class
"""

import models
from models.Model_Com import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.product import Products

class Category(BaseModel, Base):
	"""Representation of category"""
	__tablename__ = 'category'
	__table_args__ = {'extend_existing': True}
	label = Column(String(20), nullable=True)
	product_id = relationship("Products",
							   backref="product",
							   cascade="all, delete, delete-orphan")
	article_id = relationship("Article",
							   backref="article",
							   cascade="all, delete, delete-orphan")

	def __init__(self, *args, **kwargs):
		"""initializes category"""
		super().__init__(*args, **kwargs)
