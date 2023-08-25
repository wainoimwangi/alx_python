#!/usr/bin/python3
'''
python script that contains the class definition of a State
and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


'''
state class that inherits from base class
'''
class State(Base):
    '''
    State class that inherits from the base class.
    Attributes:
        id- auto-generated, unique integer, not null and a primary key
        name- string of length 128 character
    '''
    __table__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
