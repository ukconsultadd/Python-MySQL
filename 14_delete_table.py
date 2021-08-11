import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

# deleting the table (if it doesn't exists then it will give you an error)
sql_query = "DROP TABLE customers"

my_cursor.execute(sql_query)

#deleting the tanle if it exists in the db
sql_query2 = "DROP TABLE IF EXISTS customers"

my_cursor.execute(sql_query2)