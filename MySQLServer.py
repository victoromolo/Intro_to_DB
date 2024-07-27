import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("Database 'alx_book_store' already exists.")
        else:
            print(f"Failed creating database: {err}")

def main():
    try:
        # Connect to MySQL server (replace 'your_username' and 'your_password' with your MySQL credentials)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="victor2024"
        )
        cursor = conn.cursor()
        
        # Create the database
        create_database(cursor)
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    else:
        if conn.is_connected():
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
