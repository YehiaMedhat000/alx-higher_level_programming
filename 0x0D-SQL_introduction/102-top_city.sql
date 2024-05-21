-- Task: Display the top 3 cities' temperatures during July and August ordered by temperature (descending)
-- Convert Celsius to Fahrenheit using the formula (Celsius * 9/5) + 32
SELECT city, AVG(value) AS avg_temp, month
FROM temperatures
WHERE month IN (8, 7)
ORDER BY avg_temp DESC
LIMIT 3;
