-- Write your PostgreSQL query statement below
SELECT a.machine_id,ROUND(AVG(v.timestamp-a.timestamp)::numeric,3) AS processing_time 
FROM activity a JOIN activity v ON a.machine_id=v.machine_id 
WHERE a.activity_type='start' AND v.activity_type='end' 
GROUP BY a.machine_id 
ORDER BY a.machine_id ASC;
