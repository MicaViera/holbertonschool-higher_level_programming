#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists
all cities of that state."""
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
        "SELECT cities.name "
        "FROM cities "
        "LEFT JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s"
        "ORDER BY cities.id ASC", (argv[4], ))

    lists = database_cursor.fetchall()
    string = ""
    for row in lists:
        if (row != lists[0]):
            string += ", "
        string += row[0]
    print(string)

    database_cursor.close()
    database.close()
