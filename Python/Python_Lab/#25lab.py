import mysql.connector
import mysql.connector.cursor
try:
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
    )
    if connection.is_connected():
        print("connection successfully")
    cursor = connection.cursor()
    q="show databases"
    cursor.execute(q)
    result=cursor.fetchall()
    print(result)
    for i in result:
      print (i[0])
 
    q1="use sakila"
    cursor.execute(q1)
    q2= "select*from customer"
    cursor.execute(q2)
    result1=cursor.fetchall()
    for i in result1:
        print(i[1],i[2])
except mysql.connector.Error as e :
     print("error :", e)
