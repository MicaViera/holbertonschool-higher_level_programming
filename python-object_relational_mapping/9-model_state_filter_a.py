#!/usr/bin/python3
"""Script that lists all State objects that contain the letter a from
the database."""

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

    for index in session.query(State).filter(State.name.contains('a')).\
            order_by(State.id):
        print(f"{index.id}: {index.name}")

    session.close()
