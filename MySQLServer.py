import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'root',
    'password': 'my1Excellence@_94',
    'host': 'localhost',
}

try:
    # Connect to MySQL server
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Create the database
    try:
        cursor.execute("CREATE DATABASE ALX_BOOK_STORE")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("Database 'alx_book_store' already exists.")
        else:
            print(f"Failed creating database: {err}")

    # Close cursor and connection
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
