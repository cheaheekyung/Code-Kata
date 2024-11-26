-- 코드를 작성해주세요
select count(1) FISH_COUNT,
       n.FISH_NAME 	FISH_NAME
from FISH_INFO i join FISH_NAME_INFO n on i.FISH_TYPE=n.FISH_TYPE
group by 2 
order by 1 desc