#!/usr/bin/python3
"""  script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """accecing database and connecting it and retriving data from it"""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
                   FROM cities INNER JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC""", (sys.argv[4],))

    rows = cursor.fetchall()
    if rows:
        for i in range(len(rows)):
            if i != len(rows) - 1:
                print("{}, ".format(rows[i][0]), end="")
            else:
                print(rows[i][0])

    cursor.close()
    db.close()
