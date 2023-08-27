'''
script that lists all state objects from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    session_class = sessionmaker(bind=engine)
    session = session_class()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
