#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from SQL injection).
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id LIMIT 1"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

