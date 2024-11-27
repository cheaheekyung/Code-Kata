select sum(g.score) as SCORE,
        e.EMP_NO,
        e.EMP_NAME,
        e.POSITION,
        e.EMAIL
from HR_DEPARTMENT d 
join HR_EMPLOYEES e on d.DEPT_ID=e.DEPT_ID
join HR_GRADE g on e.EMP_NO=g.EMP_NO
where YEAR = 2022
group by e.EMP_NO
order by sum(g.score) desc
limit 1
