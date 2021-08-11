import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

sql_query = "DELETE FROM customers where address ='Mountain 21' ;"

my_cursor.execute(sql_query)

mydb.commit()

print(my_cursor.rowcount,"records deleted .")

#preventing sql injection attack
sql_query2 = "DELETE FROM customers WHERE address = %s"

adr_2 = ("Yellow Garden 2", )

my_cursor.execute(sql_query2, adr_2)

mydb.commit()

print(my_cursor.rowcount, "record(s) deleted")