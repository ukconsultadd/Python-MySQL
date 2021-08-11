import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

sql_query = "SELECT * FROM customers WHERE address = 'Park Lane 38';"

my_cursor.execute(sql_query)

my_result = my_cursor.fetchall()

for x in my_result:
    print(x)

print()

sql_query2 = "SELECT * FROM customers WHERE address LIKE '%way%'"

my_cursor.execute(sql_query2)

my_result2 = my_cursor.fetchall()

for x in my_result2:
  print(x)