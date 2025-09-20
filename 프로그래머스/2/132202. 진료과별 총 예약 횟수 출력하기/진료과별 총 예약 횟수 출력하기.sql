-- 코드를 입력하세요
select MCDP_CD as '진료과코드', count(*) as '5월예약건수'
from APPOINTMENT
where APNT_YMD between '2022-05-01' and '2022-05-31'
group by 1
order by 5월예약건수, 진료과코드