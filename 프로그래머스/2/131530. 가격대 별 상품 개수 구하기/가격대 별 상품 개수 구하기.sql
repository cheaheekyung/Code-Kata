-- 코드를 입력하세요
SELECT (price div 10000)*10000 PRICE_GROUP,
        count(1) PRODUCTS
from PRODUCT
group by 1
order by 1