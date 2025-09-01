select
  ugb.TITLE,
  ugb.BOARD_ID,
  ugr.REPLY_ID,
  ugr.WRITER_ID,
  ugr.CONTENTS,
  DATE_FORMAT(ugr.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD as ugb
join USED_GOODS_REPLY as ugr
  on ugb.BOARD_ID = ugr.BOARD_ID
where ugb.CREATED_DATE like '2022-10%'
order by
  ugr.CREATED_DATE,
  ugb.TITLE;
