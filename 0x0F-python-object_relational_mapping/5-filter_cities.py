#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    
    # Connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    
    # Bind the engine to the Base class, which contains the tables
    Base.metadata.create_all(engine)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session instance
    session = Session()
    
    try:
        # Query cities based on the state name provided
        cities = session.query(City).join(State).filter(State.name == state_name).order_by(City.id).all()
        
        if cities:
            for city in cities:
                print(city.name)
        else:
            print("No cities found for state '{}'".format(state_name))
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # Close the session
        session.close()

