#!/usr/bin/python3
"""Script that adds the State object “Louisiana” to the database."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                              format(username, password, db_name),
                              pool_pre_ping=True)

    session = Session(db_engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
