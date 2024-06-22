#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name,
                         port=3306)

    # Create a cursor object
    cursor = db.cursor()

    # Create the SQL query using parameterized queries
    query = "SELECT * FROM states WHERE name = '%s' ORDER BY id ASC"

    # Execute the query with the provided state name
    cursor.execute(query, (state_name,))

    # Fetch all the results
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
