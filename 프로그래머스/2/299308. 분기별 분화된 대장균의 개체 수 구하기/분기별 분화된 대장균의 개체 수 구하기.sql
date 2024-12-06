-- 코드를 작성해주세요
select concat(QUARTER(DIFFERENTIATION_DATE),'Q') as QUARTER,
        count(1) as ECOLI_COUNT
from ECOLI_DATA
group by 1
order by 1