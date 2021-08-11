import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

sql_query = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

my_cursor.execute(sql_query, adr)

my_result = my_cursor.fetchall()

for x in my_result:
  print(x)