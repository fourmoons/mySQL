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
    lines = [tuple(i) for i in lines] #list of tuples

mycursor = mydb.cursor()

mycursor.execute("SHOW columns FROM " + table)
tmp = [(column[0]) for column in mycursor.fetchall()]
headers = "("
for i in range(len(tmp) - 1):
    headers += str(tmp[i]) +  ", "
headers += str(tmp[-1]) + ")"

command = "INSERT INTO " + table + " " + str(headers) + " VALUES (%s, %s, %s)"

mycursor.executemany(command, lines)
mydb.commit()
