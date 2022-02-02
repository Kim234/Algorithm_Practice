-- 각 시간 별 입양횟수 구하기
-- having절과 where절의 다른 점은 having절은 group by절과 함께 사용해야함(바로 앞뒤로 안붙어있으면 에러)
-- 집계함수를 사용하여 조건절을 작성하거나 group by 컬럼만 조건절에 사용핤 수 있다.
SELECT HOUR(DATETIME) AS HOUR, count(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR>8 AND HOUR<20 -- 9시부터 19시까지 구하라는 조건
ORDER BY HOUR