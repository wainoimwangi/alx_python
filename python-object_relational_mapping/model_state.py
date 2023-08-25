#!/usr/bin/python3
# Write a python file that contains the class definition
# of a State and an instance Base = declarative_base():

from sqlalchemy import column, integer, string
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from the base class.
    Attributes:
        id- auto-generated, unique integer, not null and a primary key
        name- string of length 128 character
    """
    __table__ = 'State'

    id = column(integer, primary_key=True, nullable=False, autoincrement=True)
    name = column(string(128), nullable=False)
