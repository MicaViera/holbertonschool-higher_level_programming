#!/usr/bin/python3
"""Script that displays the list of values that matches the name,
safe from MySQL injections."""
import MySQLdb
from sys import argv

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
        "SELECT * FROM states "
        "WHERE BINARY name LIKE %s "
        "ORDER BY states.id ASC",
        (argv[4],))

    for row in database_cursor.fetchall():
        print(row)

    database_cursor.close()
    database.close()
