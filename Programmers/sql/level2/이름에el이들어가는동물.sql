SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog'  and NAME LIKE '%el%' -- 이름에 el이 들어가고 dog인 동물
ORDER BY NAME