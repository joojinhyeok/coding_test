-- 코드를 입력하세요
select ii.INGREDIENT_TYPE, sum(fh.TOTAL_ORDER)
from FIRST_HALF as fh join ICECREAM_INFO as ii on fh.FLAVOR = ii.FLAVOR
group by 1