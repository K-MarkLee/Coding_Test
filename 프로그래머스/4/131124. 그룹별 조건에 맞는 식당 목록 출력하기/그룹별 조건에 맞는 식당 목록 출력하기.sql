-- 코드를 입력하세요
SELECT  M.MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW R
JOIN (SELECT MEMBER_ID
     FROM REST_REVIEW
     GROUP BY MEMBER_ID
     ORDER BY COUNT(REVIEW_TEXT) DESC LIMIT 1) I
ON I.MEMBER_ID = R.MEMBER_ID
JOIN MEMBER_PROFILE M ON M.MEMBER_ID = R.MEMBER_ID
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC