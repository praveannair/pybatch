import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="myappdb"
)
mycursor = mydb.cursor()

while True:
    name = input("Enter name: ")
    email = input("Enter email: ")

    sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
    val = (name,email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    ch = input("Continue?(y/n)")
    if ch!='y':
        break
    
mycursor.execute("select * from customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

