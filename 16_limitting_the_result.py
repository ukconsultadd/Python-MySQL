import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

#returning the rows from starting 
my_cursor.execute("select * from customers limit 5 ")

my_result = my_cursor.fetchall()

for x in my_result:
    print(x)

#returning the rows from another position ,let us start from third record
#then we  have to set the offset to 2(start-1)

my_cursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

my_result2 = my_cursor.fetchall()

for x in my_result2:
    print(x)