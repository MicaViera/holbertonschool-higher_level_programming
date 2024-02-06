#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
from the database."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                              format(username, password, db_name),
                              pool_pre_ping=True)

    session = Session(db_engine)
    table = session.query(State).filter(State.name == state_name).first()

    if table:
        print(f"{table.id}")
    else:
        print("Not found")

    session.close()
