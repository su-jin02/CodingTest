-- 코드를 입력하세요
SELECT ANIMAL_TYPE, 
       IFNULL(NAME, 'No name') AS NAME, 
       SEX_UPON_INTAKE
FROM ANIMAL_INS
