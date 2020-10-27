#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import DateTime, Text, Integer, Boolean
from sqlalchemy import Column, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.sql import func

Base = declarative_base()

class SolutionsNQueens(Base):
	"""docstring for ClassName"""
	__tablename__ = 'solutions_n_queens'
	id = Column(Integer, Sequence('solutions_n_queens_id_seq'), primary_key=True)
	n_queens = Column(Integer)
	solutions = Column(Integer)
	positions = Column(Text)
	create_date = Column(DateTime(timezone=True), server_default=func.now())
	write_date = Column(DateTime(timezone=True), onupdate=func.now())
	

	def __rep__(self):
		return f"SolutionsNQueens({n_queens},{solutions},{positions})"
