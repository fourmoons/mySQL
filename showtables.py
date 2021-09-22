import mysql.connector
import os
import getpass

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password = getpass.getpass("password: "),
        database = input("database: ")
    )

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor: 
    print(x, end = " ")
