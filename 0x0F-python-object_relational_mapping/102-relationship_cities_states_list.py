#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
and includes the State name each city belongs to.
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

    # Query all cities with their associated state names using the relationship defined in City class
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close session
    session.close()

if __name__ == "__main__":
    main()

