"""
script that prints the first state object from the database
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ = "__main__":
    # check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # begin a session
    session_class = sessionmaker(bind=engine)
    session = session_class()
    # perform query
    state = session.query(State).first()
    # print result
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    # close session
    session.close()
