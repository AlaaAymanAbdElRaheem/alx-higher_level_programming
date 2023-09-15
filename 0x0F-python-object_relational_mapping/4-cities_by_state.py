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
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
