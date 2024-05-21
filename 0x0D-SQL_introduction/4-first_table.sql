-- Task: Create a table called first_table in the specified database
-- If the table first_table already exists, the script should not fail
-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
