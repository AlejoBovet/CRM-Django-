
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Informatica2023",
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# execute the SQL query using execute() method.
cursorObject.execute("CREATE DATABASE dcrm")

print("Database created successfully")