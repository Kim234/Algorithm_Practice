-- 각 animal type에 해당하는 수가 몇 마리인지
SELECT ANIMAL_TYPE, count(*) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE -- 개(dog)보다 고양이(cat)를 먼저 출력하라는 조건