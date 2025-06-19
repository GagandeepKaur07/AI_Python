import mysql.connector
from mysql.connector import Error
def create_connection():
    """funtion to create a connection to the mysql server."""
    try:
        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin'
        )
        if connection.is_connected():
            print("connected to mysql")
        return connection
    except Error as e:
        print(f"Error :{e}")
conn = create_connection()

# _____________________2_____________________
def create_database(connection):
    """function to create a database."""
    try:
        cursor= connection.cursor()
        cursor.execute("create database if not exists college_db")
        print("databse 'collage_db create successfully !")
    except Error as e:
        print(f"error : {e}")
if conn:
    create_database(conn)
    conn.close()


# ________________3____________________

def create_table(connection):
    """function to create a table inside the selected database."""
    try:
        cursor = connection.cursor()
        cursor.execute("use college_db")
        table_creation_query="""
        create table if not exists students(
        id int auto_increment primary key,
        name varchar(255) not null,
        age int not null,
        course varchar(255) not null
        )
        """
        cursor.execute(table_creation_query)
        print("table 'student' created successfuly! ")
    except Error as e:
        print("Error :", e) 
conn = create_connection()
if conn:
    create_table(conn)
    conn.close()