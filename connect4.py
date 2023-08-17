import mysql.connector as c

mydb=c.connect(
    
  host="localhost",
  user="root",
  password="root",
  database="admin"
)
if mydb.is_connected():
    print("connect successfully")
else:
    print("problem in connection")    
