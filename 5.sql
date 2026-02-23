-- 180. Consecutive Numbers

with cte as (
    select num,
    lag(num, 1) over (order by id) as prev,
    lag(num, 2) over (order by id) as sec_prev
    from Logs
)
select distinct(num) as ConsecutiveNums
from cte
where num=prev and num=sec_prev