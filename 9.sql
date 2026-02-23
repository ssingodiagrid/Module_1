-- 184. Department Highest Salary

# Write your MySQL query statement below
select d.name as Department ,e.name as Employee , max(e.salary) as Salary
from Employee as e
join Department as d
on e.departmentId= d.id
group by d.name