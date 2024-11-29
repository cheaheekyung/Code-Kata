-- 코드를 작성해주세요
select count(1) as FISH_COUNT
from FISH_INFO i join FISH_NAME_INFO n on i.FISH_TYPE=n.FISH_TYPE
where n.FISH_NAME = 'bass' or n.FISH_NAME ='snapper'