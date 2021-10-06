#UNFINISHED
#self-made attempt at creating a mySQLtable directly from a csv file
import mysql.connector 
import os 
import getpass 
import csv
from readdata import *
#create table in database from a csv file (local, root use only)
mydb = mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password = getpass.getpass("user password: "),
        database = input("database: ")
    ) 
filename = input("filename: ")
data = read_data(filename)
table_name = os.path.splitext(filename)[0]
headers = data[0]

mycursor = mydb.cursor()
command = "CREATE TABLE " + table_name + " ("

for i in range(len(headers)-1): 
    command += headers[i] + " VARCHAR(25), "
command += headers[-1] + " VARCHAR(25))"

print("Made table '" + table_name +  "' with headers: ", end = "")
[print(i, end = ", ") for i in headers[:-1]]
print(headers[-1])

mycursor.execute(command)
mydb.commit()

alldata = [tuple(i) for i in data[2:]]

mycursor.execute("SHOW columns FROM " + table_name)
tmp = [(column[0]) for column in mycursor.fetchall()]
headers = "("
for i in range(len(tmp) - 1):
    headers += str(tmp[i]) +  ", "
headers += str(tmp[-1]) + ")"

values = "("
for i in range(len(data[0]) - 1):
    values += "%s, "
values += "%s)"

command = "INSERT INTO " + table_name + " " + str(headers) + " VALUES " + values
#mycursor.executemany(command, alldata)

mydb.commit()


