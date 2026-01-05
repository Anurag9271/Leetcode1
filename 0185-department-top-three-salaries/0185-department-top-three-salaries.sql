-- Write your PostgreSQL query statement below

WITH highearner AS(SELECT e.name,e.salary,e.departmentId,d.name AS dept,DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC)AS rnk 
FROM Employee e JOIN Department d ON e.departmentId = d.id)

SELECT dept as Department,name as Employee,salary as Salary 
FROM highearner 
WHERE rnk<=3;