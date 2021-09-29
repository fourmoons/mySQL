import mysql.connector
import getpass
import sys

#some kind of workaround for LOADDATA LOCAL INFILE. For localhost root user only...

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password = getpass.getpass("password: "),
        database = input("database: ")
    )
table = input("table: ")
filename = input('filename: ')

with open(filename) as f:
    data = [x.strip() for x in f]
    lines = [i.split() for i in data]             

mycursor = mydb.cursor()
for i in range(len(lines)):
    lines[i] = tuple(lines[i])
    command = "INSERT INTO " + table + " VALUES " + str(lines[i])
   # print(command)
    mycursor.execute(command)

#[print(str(i)) for i in lines]
