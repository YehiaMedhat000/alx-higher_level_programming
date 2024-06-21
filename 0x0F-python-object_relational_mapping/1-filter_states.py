#!/usr/bin/python3
''' Script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa '''
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # SQL query to select states with names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all results of the query
    results = cursor.fetchall()

    # Print each row of the result
    for row in results:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
