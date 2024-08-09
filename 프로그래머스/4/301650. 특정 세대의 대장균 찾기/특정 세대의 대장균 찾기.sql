SELECT ed1.ID
FROM 
    ECOLI_DATA ed1 
JOIN 
    ECOLI_DATA ed2 ON ed1.PARENT_ID = ed2.ID
JOIN 
    ECOLI_DATA ed3 ON ed2.PARENT_ID = ed3.ID
WHERE 
    ed3.PARENT_ID IS NULL
ORDER BY ed1.ID