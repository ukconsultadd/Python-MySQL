import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    port = '3306',
    user = 'root',
    password = 'rootpass'
)

my_cursor = mydb.cursor()

#creating database
my_cursor.execute("CREATE DATABASE mydatabase")

#showing databases
my_cursor.execute("SHOW DATABASES")

for x in my_cursor:
    print(x)

