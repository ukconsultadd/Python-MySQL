import mysql.connector as connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpass",
    database = "mydatabase",
    port='3306'
)

my_cursor = mydb.cursor()

#using inner join,finding the rows where there is a match
sql_query = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

my_cursor.execute(sql_query)  

my_result = my_cursor.fetchall()

for x in my_result:
  print(x)

print('\n\n')

#finding the rows with all the users whether they have some fav or not(left join)
sql_query2 = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

my_cursor.execute(sql_query2)  

my_result2 = my_cursor.fetchall()

for x in my_result2:
  print(x)

print('\n\n')

#Select all products, and the user(s) who have them as their favorite:(right join)
sql_query3 = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"

my_cursor.execute(sql_query3)  

my_result3 = my_cursor.fetchall()

for x in my_result3:
  print(x)