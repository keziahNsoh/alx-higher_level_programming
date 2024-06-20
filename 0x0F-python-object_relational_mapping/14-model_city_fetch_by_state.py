#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database_name))

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session to communicate with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities and their associated states, ordered by city id
    cities = session.query(City).order_by(City.id).all()

    # Print results as "<state name>: (<city id>) <city name>"
    for city in cities:
        state_name = session.query(State).filter_by(id=city.state_id).one().name
        print("{}: {}".format(state_name, city))

    session.close()

