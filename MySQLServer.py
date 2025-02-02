import mysql.connector
from mysql.connector import Error


def create_database():
    try:
       db = mysql.connector.connect(
           host="localhost",
           user="root",
           password="mypassword",
       )
       
       if db.is_connected():
          cursor = db.cursor()
          sql = 'CREATE DATABASE IF NOT EXISTS alx_book_store'
          cursor.execute(sql)
          print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error: Could not connect to MySQL server - {e}")
    
    finally:
        if db.is_connected():
            cursor.close()
            db.close()
            

if __name__ == "__main__":
    create_database()            


