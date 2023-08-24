#!/usr/bin/python3
"""
script that takes in the name of a state as an
argument and lists all cities of that state
using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    conncet to database
    """
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    """
    connect to cursor
    """
    cursor = db.cursor()
    """
    write an Sql query and execute
    """
    cursor.execute("SELECT cities.id, cities.name, states.id\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")
    """
    fetch and display results
    """
    [print(city) for city in cursor.fetchall() if state[1] == sys.argv[4]]
    """
    close cursor and database
    """
    cursor.close()
    db.close()
