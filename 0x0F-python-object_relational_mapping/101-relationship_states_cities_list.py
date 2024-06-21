#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def main():
    """Main function for the script."""
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        return

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Database connection
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states with their cities using the relationship defined in State class
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close session
    session.close()

if __name__ == "__main__":
    main()

