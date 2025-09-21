-- 코드를 작성해주세요
select
    C.ID,                         -- 자식의 ID
    C.GENOTYPE,                   -- 자식의 형질
    P.GENOTYPE as PARENT_GENOTYPE -- 부모의 형질
from ECOLI_DATA as C -- ECOLI_DATA 테이블을 '자식(Child)'으로 사용
join ECOLI_DATA as P ON C.PARENT_ID = P.ID -- ECOLI_DATA 테이블을 '부모(Parent)'로 사용해 JOIN
WHERE (C.GENOTYPE & P.GENOTYPE) = P.GENOTYPE -- 자식의 형질과 부모의 형질을 AND 연산한 결과가 부모의 형질과 같은 경우(2진수 고려안하고 &로 처리)
order by C.ID; -- ID 기준 오름차순 정렬