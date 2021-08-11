import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
my_cursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", my_cursor.lastrowid)