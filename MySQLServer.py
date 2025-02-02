import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Change this to your MySQL server host if needed
            user='root',  # Change this to your MySQL user
            password='my1Excellence@_94'  # Change this to your MySQL password
        )

        # Check if the connection is successful
        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle connection or execution errors
        print(f"Error: {e}")

    finally:
        # Close the connection if it's open
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


# Call the function to create the database
create_database()
