-- Task: List all records with a score >= 10 from the table second_table
-- Select and display both the score and the name, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
