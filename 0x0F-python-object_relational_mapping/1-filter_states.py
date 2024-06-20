#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to fetch id and name columns
    sql = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id LIMIT 2"

    try:
        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows
        results = cursor.fetchall()

        # Print each row
        for row in results:
            print(row)

    except Exception as e:
        print("Error:", e)

    # Disconnect from server
    db.close()

