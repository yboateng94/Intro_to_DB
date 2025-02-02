import mysql.connector

# Database connection details (replace with your own)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="my1Excellence@_94",
    database="alx_book_store"
)

mycursor = mydb.cursor()


# Create the SQL schema for the "alx_book_store" database.

def create_sql_schema():
    sql_script = """
    -- Create the database
    CREATE DATABASE IF NOT EXISTS alx_book_store;
    USE alx_book_store;

    -- Create the Authors table
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INT AUTO_INCREMENT PRIMARY KEY,
        author_name VARCHAR(215) NOT NULL
    );

    -- Create the Books table
    CREATE TABLE IF NOT EXISTS Books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(130) NOT NULL,
        author_id INT,
        price DOUBLE NOT NULL,
        publication_date DATE,
        FOREIGN KEY (author_id) REFERENCES Authors(author_id) ON DELETE SET NULL
    );

    -- Create the Customers table
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(215) NOT NULL,
        email VARCHAR(215) NOT NULL,
        address TEXT
    );

    -- Create the Orders table
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        order_date DATE NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
    );

    -- Create the Order_Details table
    CREATE TABLE IF NOT EXISTS Order_Details (
        orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
        order_id INT,
        book_id INT,
        quantity DOUBLE NOT NULL,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
        FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE CASCADE
    );
    """

    # Write the SQL script to a file
    with open("alx_book_store.sql", "w") as file:
        file.write(sql_script)
    print("SQL schema has been written to 'alx_book_store.sql'.")

# Run the function to generate the SQL script
create_sql_schema()
