import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

sql_query = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

my_cursor.execute(sql_query)

mydb.commit()

print(my_cursor.rowcount, "record(s) affected")

#prevent sql injection

sql_query2 = "UPDATE customers SET address = %s WHERE address = %s"
value = ("Valley 345", "Canyon 123")

my_cursor.execute(sql_query2, value)

mydb.commit()

print(my_cursor.rowcount, "record(s) affected")