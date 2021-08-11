import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

#inserting multiple rows in a single query at once 
sql_query = "INSERT INTO customers (name, address) VALUES (%s, %s)"

#val variable carrying multiple row values
values = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

#executing the sql query using executemany method of cursor object
my_cursor.executemany(sql_query,values)

#committing the database
mydb.commit()

print(str(my_cursor.rowcount) + " rows/records inserted...")

#returning last inserted row id
print(" last record inserted ID: ", my_cursor.lastrowid)

