#!/usr/bin/python3
"""
script that takes in an argument and
displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    # Establish a connection to the MySQL server
    """
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         state_name=sys.argv[4])
    """
    Create a cursor to interact with the database
    """
    cursor = db.cursor()
    """
    Execute the SQL query to retrieve states
    """
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    """
    fetch and display the results
    """
    [print("state {}".format(state_name)) for state in cursor.fetchall()]
    """
    Close the cursor and the database connection
    """
    cursor.close()
    db.close()
