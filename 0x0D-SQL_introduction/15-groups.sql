-- Lists the number of records with the same score in the table
SELECT score , COUNT(score) AS number FROM second_table
GROUP BY Score
ORDER BY number DESC;
