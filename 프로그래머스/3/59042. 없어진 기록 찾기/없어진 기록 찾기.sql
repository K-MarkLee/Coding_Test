-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O LEFT JOIN ANIMAL_INS I ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME IS NOT NULL AND I.ANIMAL_ID IS NULL