-- 코드를 입력하세요
SELECT DATE_FORMAT(S.SALES_DATE,'%Y')AS YEAR,DATE_FORMAT(S.SALES_DATE, '%m') AS MONTH, 
U.GENDER, COUNT(DISTINCT(S.USER_ID)) AS USERS
FROM ONLINE_SALE S
LEFT JOIN USER_INFO U
ON S.USER_ID = U.USER_ID
WHERE !ISNULL(U.GENDER)
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER