-- Task: List all records of the table second_table with a name value
-- Select and display the score and name, excluding rows with empty names, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
