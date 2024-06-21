#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' (upper N)
from the database hbtn_0e_0_usa.

"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to retrieve states starting with 'N'
    query = """
            SELECT id, name
            FROM states
            WHERE name LIKE 'N%'
            ORDER BY id ASC
            """

    try:
        # Execute the SQL command
        cursor.execute(query)

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Print each row (id, name)
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Disconnect from server
        cursor.close()
        db.close()

