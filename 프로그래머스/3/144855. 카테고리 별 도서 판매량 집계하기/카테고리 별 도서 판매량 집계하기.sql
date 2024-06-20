-- 코드를 입력하세요
SELECT CATEGORY,SUM(SALES) AS TOTAL_SALES
FROM BOOK_SALES AS S
JOIN BOOK AS B ON B.BOOK_ID = S.BOOK_ID
WHERE DATE_FORMAT(SALES_DATE,"%Y-%m") = '2022-01'
GROUP BY CATEGORY
ORDER BY CATEGORY