-- Use the database passed as an argument
["USE alx_book_store";]

-- Query to get the full description (columns and their details) of the 'books' table
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_DEFAULT, 
    EXTRA
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = '["TABLE_SCHEMA = 'alx_book_store'"]
    AND TABLE_NAME = 'Books';
