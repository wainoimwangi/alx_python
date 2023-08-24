#!/usr/bin/python3
"""
script that lists all cities from database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    connect to database
    """
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    """
    create cursor for database
    """
    cursor = db.cursor()
    """
    execute the sql query
    """
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities\
                    INNER JOIN states\
                    ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")
    """
    fetch and display results
    """
    [print(city) for city in cursor.fetchall()]
    """
    close database and cursor
    """
    cursor.close()
    db.close()
