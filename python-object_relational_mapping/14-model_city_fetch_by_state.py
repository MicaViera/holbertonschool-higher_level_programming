#!/usr/bin/python3
"""Script that prints all City objects from the database."""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    session = Session(db_engine)

    for state_table, city_table in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all():
        print(f"{state_table.name}: ({city_table.id}) {city_table.name}")

    session.close()
