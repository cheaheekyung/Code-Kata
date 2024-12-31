-- 코드를 입력하세요
SELECT u.USER_ID, 
        u.NICKNAME, 
        concat(u.CITY," ",u.STREET_ADDRESS1," ",u.STREET_ADDRESS2)'전체주소', 
        concat(substr(u.TLNO,1,3),'-',
               substr(u.TLNO,4,4),'-',
               substr(u.TLNO,8,4))as '전화번호'
from USED_GOODS_BOARD b join USED_GOODS_USER u on b.WRITER_ID=u.USER_ID
group by 1,2
having count(u.USER_ID)>2
order by 1 desc