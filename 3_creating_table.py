import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    port = '3306',
    user = 'root',
    password = 'rootpass',
    database = "mydatabase"
)

my_cursor = mydb.cursor()

#creating tables in mydatabase

#showing the tables in mydatabase
my_cursor.execute("SHOW TABLES")

table_list = []

table_lists = list(my_cursor)
if len(table_lists)!=0:
    table_list = table_lists[0]

if  "customers" not in table_list :
    my_cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    print("Table successfully created")
else:
    print("Table already existed")