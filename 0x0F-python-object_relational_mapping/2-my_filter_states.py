#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to retrieve states matching the provided name
        query = """
                SELECT id, name
                FROM states
                WHERE name = %s
                ORDER BY id ASC
                """

        # Execute the SQL command with the user-provided state_name
        cursor.execute(query, (state_name,))

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Print each row (id, name)
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()

