-- 코드를 입력하세요
SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A
JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
JOIN PATIENT P ON A.PT_NO = P.PT_NO
WHERE DATE_FORMAT(A.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
AND APNT_CNCL_YN = 'N'
ORDER BY APNT_YMD