-- Write your PostgreSQL query statement below
WITH rank AS(
    SELECT *,DENSE_RANK() OVER (ORDER BY salary DESC)AS rnk 
    FROM employee
)
SELECT MAX(CASE WHEN rnk=2 THEN salary ELSE null END) AS SecondHighestSalary 
FROM rank;


-- SELECT COALESCE((SELECT DISTINCT salary
-- FROM employee
-- ORDER BY salary DESC
-- OFFSET 1 LIMIT 1),null) AS SecondHighestSalary;

