# Write your MySQL query statement below
SELECT A.name as Employee
FROM Employee as A
JOIN Employee as B
ON B.id = A.managerId
WHERE A.salary > B.salary