'''
python script that contains the class definition of a State
and an instance Base = declarative_base()
'''
# import sqlalchemy modules
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# define the declarative base class
Base = declarative_base()


# create a class state that inherits from base class
class State(Base):
    '''
        State class that inherits from the base class.
        Attributes:
            id- auto-generated, unique integer, not null and a primary key
            name- string of length 128 character
        Return the class table metadata
    '''
    # define the table name
    __tablename__ = "states"
    # set the column of the states table
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
