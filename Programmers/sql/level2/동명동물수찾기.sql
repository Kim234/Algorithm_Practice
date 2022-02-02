-- 동명인 동물 수 찾기
SELECT NAME, count(*) AS count
FROM ANIMAL_INS
GROUP BY NAME
HAVING count(*)>=2 and NAME IS NOT NULL -- 조건: 두 마리 이상, 이름이 없는 경우 제외 
ORDER BY NAME