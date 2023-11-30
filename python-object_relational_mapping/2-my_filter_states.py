#!/usr/bin/python3
"""Script that lists all states with a name starting with N."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_password,
        database=database_name
    )

    database_cursor = database.cursor()
    database_cursor.execute(
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY states.id ASC".format(state_name_searched)
    )

    for row in database_cursor:
        print(row)

    database_cursor.close()
    database.close()
