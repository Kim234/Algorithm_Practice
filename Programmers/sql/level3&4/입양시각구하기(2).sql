-- 해당 시각에 입양된 기록이 없어도(NULL이어도) COUNT 0으로 출력하는 것이 관건
SET @HOUR_LIST = -1;
SELECT
(@HOUR_LIST := @HOUR_LIST +1) AS 'HOUR',
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR_LIST) AS 'COUNTS'
FROM ANIMAL_OUTS
WHERE @HOUR_LIST < 23

-- 해결 방식
-- SET으로 HOUR_LIST라는 변수 선언하고 +1씩 하며 0~23시까지 모든 시간에 대한 COUNT 출력