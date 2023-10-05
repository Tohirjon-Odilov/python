-- 182 dublicate emails
SELECT email as Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;


-- 196 delete dublicate email
delete p1 from Person p1, Person p2 
where p1.Id > p2.Id and p1.Email = p2.Email;


-- 1693 daliy lead and partners
SELECT 
    date_id, make_name, 
    COUNT(DISTINCT lead_id) AS unique_leads, 
    COUNT(DISTINCT partner_id) AS unique_partners 
FROM 
    DailySales 
GROUP BY 
    date_id, make_name
