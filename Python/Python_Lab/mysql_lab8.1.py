import mysql.connector
connection = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="admin",
    database=""
) 
if connection.is_connected():
    print("successfully connected to mysql ")
else:
    print("failed to connect to mysql")
