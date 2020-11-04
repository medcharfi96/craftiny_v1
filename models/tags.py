#!/usr/bin/python3
"""
add tag tag table to db
"""

import models
from models.Model_Com import BaseModel, Base, String
import sqlalchemy
from sqlalchemy import Column, String

class Tag(BaseModel, Base):
	"""Representation of tags"""
	__tablename__ = 'tags'
	__table_args__ = {'extend_existing': True}
	label = Column(String(20), nullable=True)

	def __init__(self, *args, **kwargs):
		"""initializes tags"""
		super().__init__(*args, **kwargs)
