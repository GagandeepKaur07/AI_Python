import mysql.connector
from mysql.connector import Error
def create_connection():
    """create a connetion to mysql"""
    try:
        connection= mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='college_db'
        )
        if connection.is_connected():
            print("successfully connected to mysql server.")
        return connection
    except Error as e:
        print(f"Error :{e}")
        return None
def insert_student_data(connection):
    """insert multiple student records into the 'students'."""
    try:
        cursor= connection.cursor()
        insert_query="""
        insert into students(name,age,course)
        values(%s, %s, %s)
        """
        students_data=[
            ('sidhart',20,'computer science'),
            ('maria',22,'mathematics'),
            ('ravi',21,'bio')
        ]
        cursor.executemany(insert_query,students_data)
        connection.commit()
        print(f"{cursor.rowcount} records(s) inserted successfully into the students table, ")
    except Error as e:
        print(f"Error : {e}")
def main():
    connection=create_connection()
    if connection:
        insert_student_data(connection)
        connection.close()
        print("MYSQL connection closed")
if __name__ == "__main__":
    main()