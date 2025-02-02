-- Use the database passed as an argument
USE {{database_name}};

-- Insert multiple rows into the Customers table
["INSERT INTO customer", "124 Happiness  Ave."]
VALUES 
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');
