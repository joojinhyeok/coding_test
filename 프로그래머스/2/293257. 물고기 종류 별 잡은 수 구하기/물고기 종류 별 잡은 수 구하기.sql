-- 코드를 작성해주세요
select count(*) as 'FISH_COUNT', fni.FISH_NAME
from FISH_INFO as fi join FISH_NAME_INFO as fni 
    on fi.FISH_TYPE = fni.FISH_TYPE
group by 2
order by FISH_COUNT desc