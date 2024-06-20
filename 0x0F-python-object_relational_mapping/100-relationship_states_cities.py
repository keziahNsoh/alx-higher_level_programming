#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
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

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Database connection with pool_pre_ping=True to handle reconnections
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}', pool_pre_ping=True)
    
    # Create all tables if they don't exist
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add objects to session and commit changes
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close session
    session.close()

if __name__ == "__main__":
    main()

