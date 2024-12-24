-- 코드를 입력하세요
SELECT CATEGORY,
        max(price) MAX_PRICE,
        PRODUCT_NAME
from FOOD_PRODUCT as f
where CATEGORY in ('과자', '국', '김치', '식용유') and
    price = (select max(price) from FOOD_PRODUCT as p where f.category=p.category)
group by CATEGORY
order by 2 desc