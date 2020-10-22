#!/usr/bin/python3
"""

"""

import models
from models.Model_Com import BaseModel, Base, String
import sqlalchemy
from sqlalchemy import Column, String

class Tag(Base, BaseModel):
	"""Representation of tags"""
	__tablename__ = 'tags'
	__table_args__ = {'extend_existing': True}
	label = Column(String(20), nullable=True)

	def __init__(self, *args, **kwargs):
		"""initializes user"""
		super().__init__(*args, **kwargs)
