#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states, sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result of the query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
