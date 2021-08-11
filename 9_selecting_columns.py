import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

my_cursor.execute("SELECT name, address,id FROM customers;")

print(str(my_cursor.fetchone())+ "haha")

my_result = my_cursor.fetchall()

for x in my_result:
    print(x)

