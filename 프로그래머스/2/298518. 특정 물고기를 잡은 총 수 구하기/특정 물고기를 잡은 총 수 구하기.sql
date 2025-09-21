-- 코드를 작성해주세요
select count(*) as 'FISH_COUNT'
from FISH_INFO as fi join FISH_NAME_INFO as fni on fi.FISH_TYPE = fni.FISH_TYPE
where fni.FISH_NAME = 'BASS' or fni.FISH_NAME = 'SNAPPER'