# Write your MySQL query statement below
# x+y > z and y+z > x and x+z > y then its form a triangle
SELECT
   x, y, z,
   CASE 
    WHEN x+y > z and y+z > x and x+z > y THEN 'Yes'
    ELSE 'No'
    END AS triangle
FROM
    Triangle;