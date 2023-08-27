"""
script that prints the first state object from the database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ = "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), 
                           pool_pre_ping=True)

    session_class = sessionmaker(bind=engine)
    session = session_class()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    
    session.close()