"""
script that prints the first state object from the database
"""


if __name__ = "__main__":
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # begin a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # perform query
    state = session.query(State).order_by(State.id).first()
    # print result
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    # close session
    session.close()
