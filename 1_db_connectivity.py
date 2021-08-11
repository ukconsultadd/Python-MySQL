import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    port = '3306',
    user = 'root',
    password = 'rootpass'
)

print(mydb)