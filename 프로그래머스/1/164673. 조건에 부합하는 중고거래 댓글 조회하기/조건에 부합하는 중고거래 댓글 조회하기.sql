-- 코드를 입력하세요
SELECT UGB.TITLE,
       UGB.BOARD_ID, 
       UGR.REPLY_ID, 
       UGR.WRITER_ID,
       UGR.CONTENTS,
       DATE_FORMAT(UGR.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD AS UGB
JOIN USED_GOODS_REPLY AS UGR
ON UGB.BOARD_ID = UGR.BOARD_ID
WHERE YEAR(UGB.CREATED_DATE) = 2022 and MONTH(UGB.CREATED_DATE) = 10
ORDER BY UGR.CREATED_DATE, UGB.TITLE