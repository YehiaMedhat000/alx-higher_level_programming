-- Task: Display the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Convert Celsius to Fahrenheit using the formula (Celsius * 9/5) + 32
SELECT city, AVG((value * 9/5) + 32) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
