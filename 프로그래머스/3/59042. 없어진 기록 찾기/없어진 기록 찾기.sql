-- 코드를 입력하세요
SELECT o.ANIMAL_ID,
        o.NAME
from ANIMAL_INS i right join ANIMAL_OUTS o on i.ANIMAL_ID=o.ANIMAL_ID
where o.DATETIME is not null and i.DATETIME is null
