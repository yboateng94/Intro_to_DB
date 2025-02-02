import mysql.connector

# Database connection details (replace with your own)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="my1Excellence@_94",
    database="alx_book_store"
)

mycursor = mydb.cursor()
