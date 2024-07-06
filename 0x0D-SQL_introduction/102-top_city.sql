-- Displays the top 3 of cities temperatures during july and augest
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
