#!/usr/bin/python3
"""

"""

import models
from models.Model_Com import BaseModel, Base, DateTime
import sqlalchemy
from sqlalchemy import Column, String
from datetime import datetime

class Category(Base, BaseModel):
	"""Representation of category"""
	__tablename__ = 'category'
	__table_args__ = {'extend_existing': True}
	label = Column(String(20), nullable=True)

	def __init__(self, *args, **kwargs):
		"""initializes user"""
		super().__init__(*args, **kwargs)
