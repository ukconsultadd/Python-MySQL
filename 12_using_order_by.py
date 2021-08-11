import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

#selecting rows in ascending order of name
sql_query = "SELECT * FROM customers ORDER BY name"

my_cursor.execute(sql_query)

my_result = my_cursor.fetchall()

for x in my_result:
  print(x)


print("\n\n")
#selecting the rows in descending order of name
sql_query2 = "SELECT * from customers order by name desc;"

my_cursor.execute(sql_query2)

my_result2 = my_cursor.fetchall()

for y in my_result2:
  print(y)