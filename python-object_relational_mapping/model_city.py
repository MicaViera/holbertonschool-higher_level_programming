#!/usr/bin/python3
"""File that contains te class definition of a City and an instance."""
from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City class."""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
