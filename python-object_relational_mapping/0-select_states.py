#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa."""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        database=database_name
    )

    database_cursor = database.cursor()
    database_cursor.execute(
        "SELECT * FROM states ORDER BY states.id ASC"
    )

    for row in database_cursor:
        print(row)

    database_cursor.close()
    database.close()
