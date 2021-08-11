import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

#executing query to select all the rows
my_cursor.execute("SELECT * FROM customers;")

#fetching the next row of a query result set
print(my_cursor.fetchone())
print(my_cursor.fetchone())
print(my_cursor.fetchone())
print(my_cursor.fetchone())
print(my_cursor.fetchone())


my_result = my_cursor.fetchall()

for x in my_result:
    print(x)

print(type(my_result[0]))