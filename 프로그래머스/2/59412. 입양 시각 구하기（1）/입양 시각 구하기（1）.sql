-- 코드를 입력하세요
select hour(DATETIME) as 'HOUR', count(*) as 'COUNT'
from ANIMAL_OUTS
where hour(DATETIME) between '9' and '20'
group by 1
order by HOUR