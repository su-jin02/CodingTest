-- 코드를 작성해주세요
SELECT ID,FISH_NAME,LENGTH
FROM FISH_INFO AS I
INNER JOIN FISH_NAME_INFO AS N
ON I.FISH_TYPE = N.FISH_TYPE
WHERE (I.FISH_TYPE, I.LENGTH) IN (
    SELECT FISH_TYPE, MAX(LENGTH)
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)
ORDER BY ID