"""
script that lists all state objects that contain letter a
"""


if __name__ == "__main__":
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    # begin a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # perform query
    all_states = session.query(State).order_by(State.id).all()
    for state in all_states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    # close session
    session.close()
