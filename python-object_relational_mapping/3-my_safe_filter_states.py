#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

def safe(user, passwd, db, state_name):
    """
    Establish a connection to the MySQL server
    """
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    """
    Create a cursor to interact with the database
    """
    cursor = db.cursor()
    """
    Execute the SQL query to retrieve states
    """
    state_name = sys.argv[4]
    cursor.execute("SELECT * FROM states \
                    WHERE BINARY name = '{}'".format(state_name))
    """
    fetch and display the results
    """
    [print(state) for state in cursor.fetchall()]
    """
    Close the cursor and the database connection
    """
    cursor.close()
    db.close()

if __name__ == "__main__":
    safe()
