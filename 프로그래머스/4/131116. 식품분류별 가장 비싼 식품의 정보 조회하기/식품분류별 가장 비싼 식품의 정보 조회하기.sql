-- 코드를 입력하세요
SELECT CATEGORY,
        PRICE MAX_PRICE,
        PRODUCT_NAME
from FOOD_PRODUCT p
where CATEGORY in ('과자', '국', '김치', '식용유') 
and price = (
        select max(PRICE) from FOOD_PRODUCT pr where p.CATEGORY=pr.CATEGORY)

order by 2 desc