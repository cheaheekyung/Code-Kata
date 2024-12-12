SELECT WAREHOUSE_ID,
       WAREHOUSE_NAME,
       ADDRESS,
       if (freezer_yn is null, "N", freezer_yn) 'FREEZER_YN'
from FOOD_WAREHOUSE
where address like '경기도%' 
order by warehouse_id