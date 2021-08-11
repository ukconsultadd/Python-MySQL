import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

#inserting row using query and values separately
sql_query = "INSERT INTO customers (name, address) VALUES (%s, %s)"
value = ("Johny", "Highway 22")

my_cursor.execute(sql_query,value)

#committing the changes
mydb.commit()

#cursor.rowcount returns the number of rows/records inserted
print(my_cursor.rowcount, "record inserted...")

#inserting row using query and values together in single string
sql_query_2 = """INSERT INTO customers (name,address)  VALUES('UJJWAL KANSAL' , 'MODINAGAR' )"""

#executing the sql_query2
my_cursor.execute(sql_query_2)

#committing the changes
mydb.commit()

#cursor.rowcount returns the number of rows/records inserted
print(my_cursor.rowcount, "record inserted...")
