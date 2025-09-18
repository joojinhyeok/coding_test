-- 코드를 작성해주세요
select ii.ITEM_ID as ITEM_ID, ii.ITEM_NAME as ITEM_NAME, ii.RARITY as RARITY
from ITEM_INFO as ii join ITEM_TREE as it 
    on ii.ITEM_ID = it.ITEM_ID
where ii.ITEM_ID in (
        select it.ITEM_ID
        from ITEM_TREE as it
        where it.PARENT_ITEM_ID in(
                select ii.ITEM_ID
                from ITEM_INFO as ii
                where RARITY = 'RARE'))
order by ii.ITEM_ID desc