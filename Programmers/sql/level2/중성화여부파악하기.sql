-- 이름에 Neutered나 Spayed가 들어가면 중성화
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE '%Neutered%' or SEX_UPON_INTAKE LIKE '%Spayed%', 'O','X') AS '중성화'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID