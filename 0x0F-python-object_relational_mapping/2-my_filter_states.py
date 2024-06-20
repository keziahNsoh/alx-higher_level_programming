#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument Arizona.
"""

#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id LIMIT 1"
    try:
        # Execute the SQL command
        cursor.execute(sql, (state_name,))
        # Fetch the first row
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            print("No matching state found")
    except Exception as e:
        print("Error:", e)

    # Disconnect from server
    db.close()

