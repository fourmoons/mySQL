import mysql.connector
import getpass
#add primary key to table
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = getpass.getpass("password: "),
        database = input("database: ")
    )

table = input("table: ")
mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE " + table + "  ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
