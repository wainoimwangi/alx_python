#!/usr/bin/python3
"""
Write a python file that contains the class definition
of a State and an instance Base = declarative_base():

State class:
    inherits from Base Tips
    links to the MySQL table states
    class attribute id that represents
    a column of an auto-generated, unique integer, not null and is a primary key
    class attribute name that represents a
    column of a string with maximum 128 characters and not null
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)
"""
from sqlalchemy import create_engine, column, integer, string, sequence
from sqlalchemy.ext.declarative import declarative_base



"""
declare a mapping
"""
Base = declarative_base()


"""
    define class State that inherits from declarative base()
"""
class State(Base):
    """
        State class that inherit from the base class.
        Attributes:
            id- auto-generated, unique integer, not null and a primary key
            name- string of length 128 character
    """
    __table__ = 'State'

    id = column(integer, primary_key=True, nullable=False, autoincrement=True)
    name = column(string(128), nullable=False)
