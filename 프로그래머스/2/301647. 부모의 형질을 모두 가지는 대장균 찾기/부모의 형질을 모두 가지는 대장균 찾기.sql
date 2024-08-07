-- 코드를 작성해주세요
SELECT 
    ed1.ID, 
    ed1.GENOTYPE, 
    ed2.GENOTYPE AS PARENT_GENOTYPE
FROM 
    ECOLI_DATA ed1 
JOIN 
    ECOLI_DATA ed2 ON ed1.PARENT_ID = ed2.ID
WHERE 
    (ed1.GENOTYPE | ed2.GENOTYPE) = ed1.GENOTYPE
ORDER BY ed1.ID