#!/usr/bin/python3
"""
Python script that retrieves and displays all states with names starting with 'N'
(upper case 'N') from the hbtn_0e_0_usa database using the MySQLdb module
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
                         db=sys.argv[3])
    """
    Create a cursor to interact with the database
    """
    cursor = db.cursor()
    """
    Execute the SQL query to retrieve states
    """
    cursor.execute("SELECT * FROM states WHERE name LIKE '%N%' ORDER BY states.id ASC")
    """
    fetch and display the results
    """
    [print(state) for state in cursor.fetchall()]
    """
    Close the cursor and the database connection
    """
    cursor.close()
    db.close()