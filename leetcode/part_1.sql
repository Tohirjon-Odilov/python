-- 182 dublicate emails
SELECT email as Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;


-- 196 delete dublicate email
delete p1 from Person p1, Person p2 
where p1.Id > p2.Id and p1.Email = p2.Email;

-- 197. Rising Temperature
SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature
AND DATEDIFF(w1.recordDate, w2.recordDate) = 1;
-- Bu so'rovda, Weather jadvalidan id qiymatlarini olish uchun foydalanilgan va uning shartlari quyidagicha:

--     Shartlar bo'yicha, w1.temperature (birinchi kundagi harorat) w2.temperature (oldingi kundagi haroratdan) katta bo'lishi kerak.
--     DATEDIFF funksiyasi yordamida w1.recordDate va w2.recordDate orasidagi kunlar farq 1 ga teng bo'lishi kerak, ya'ni bu ikki qatorning kunlari bir-biriga o'xshash bo'lishi kerak.

-- Bu so'rovning natijasi, bir kunidan keyin haroratning oshishini ko'rsatadigan id qiymatlari ro'yxati bo'ladi.

-- 511. Game Play Analysis I
SELECT player_id, MIN(event_date) firs_login
FROM Activity
GROUP BY player_id;

-- 1693 daliy lead and partners
SELECT 
    date_id, make_name, 
    COUNT(DISTINCT lead_id) AS unique_leads, 
    COUNT(DISTINCT partner_id) AS unique_partners 
FROM 
    DailySales 
GROUP BY 
    date_id, make_name


