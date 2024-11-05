import mysql.connector #pip install mysql-connector-python

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE myappdb")


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="myappdb"
# )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), email VARCHAR(255))")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="myappdb"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val = ("Ria", "ria@gmail.com")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")




