# Install Mysql on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1029384756'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a dataBase
cursorObject.execute("CREATE DATABASE chatdb")

print("done")
