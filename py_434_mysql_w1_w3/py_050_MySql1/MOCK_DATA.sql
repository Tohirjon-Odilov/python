-- Databzalarni ko'rish.
SHOW DATABASES;

-- Databazani yasash.
CREATE DATABASE myfirst_db;
SHOW DATABASES;

-- aziz_shakirov - snake case
-- azizShakirov - camel case
-- AzizShakirov - pascal case

-- Databazani o'chirish.
DROP DATABASE myfirstdb;
SHOW DATABASES;


CREATE DATABASE universitydb;
SHOW DATABASES;

--Databazaga ulanish
USE universitydb;

---||| ctrl + l yoki ctrl + k ekran tozalash. |||---

--Jadvallarni ko'rish.
SHOW TABLES;

-- Jadval yasash.
CREATE TABLE student (
    first_name VARCHAR(64),
    second_name VARCHAR(64),
    age INTEGER,
    gender VARCHAR(8)
);

SHOW TABLES;

-- jadvalni qayta nomlash.
RENAME TABLE student TO talaba;  
SHOW TABLES;

-- jadvalni o'chirish.
DROP TABLE talaba;
SHOW TABLES;

CREATE TABLE IF NOT EXISTS student (  
    id INT NOT NULL AUTO_INCREMENT,  
    first_name VARCHAR(32) NOT NULL,  
    second_name VARCHAR(32) NOT NULL,  
    age INT NOT NULL,  
    gender TEXT,
    phone_number VARCHAR(13),
    PRIMARY KEY (id)  
);  

--jadvaldagi fieldlarni tiplarini ko'rish.
DESCRIBE student;
DESC student;
SHOW COLUMNS FROM universitydb.student;
SHOW COLUMNS FROM student IN universitydb;

-- jadvalni to'liq ko'rish.
SELECT *FROM student;

-- jadvalni to'ldirish. 1 - usul. bir qatorli.
INSERT INTO student (first_name, second_name, age, gender, phone_number) 
VALUES ('Anvar', 'Rahimov', 25, 'MALE', '+998901234567');

INSERT INTO student (first_name, second_name, gender, age, phone_number) 
VALUES ('Bunyod', 'Baxromov', 'MALE', 17, '+998901234567');

-- jadvalni to'ldirish. Hato. phone_numberda 13tadan ko'p belgi kiritib bo'lmaydi.
INSERT INTO student (first_name, second_name, age) 
VALUES 
('Feruza', 'Bahromova', 100);

-- jadvalni to'ldirish. 2 - usul. ko'p qatorli.
INSERT INTO student (first_name, second_name, age, gender, phone_number) VALUES
('Gayrat', 'Bahromov', 31, 'MALE', '+998924324362'),
('Murodjon', 'Javlonov', 21, 'MALE', '+998902316985'),
('Zulfiya', 'Bahromova', 22, 'FEMALE', '+998924324361'),
('Muqaddam', 'Latipova', 23, 'FEMALE', '+998974324363'),
('Hamiddulla', 'Kamilov', 25, 'MALE', '+998974324364'),
('Jackie', 'Chan', 40, 'MALE', '+912341000011'),
('Aziz', 'Shakirov', 16, 'MALE', '+998924314365'),
('Toxir', 'Jalilov', 22, 'MALE', '+998984424363'),
('Gulom', 'Haydar', 28, 'MALE', '+998974376653'),
('Asal', 'Vohidova', 22, 'FEMALE', NULL),
('Qobil', 'Hasanov', 32, 'MALE', '+998954326664'),
('Jan-Clod', 'van Damm', 63, 'MALE', '+955332226677'),
('Botir', 'Zokirov', 19, 'MALE', '+998954345365'),
('Malika', 'Yuldasheva', 235, 'FEMALE', '+998934324311'),
('Juma', 'Kamilov', 16, 'MALE', '+998924324322'),
('Aziza', 'Zokirova', 20, 'FEMALE', '+998941314333'),
('Jumagul', 'Bozorova', 27, 'FEMALE', '+998934324344'),
('Aziz', 'Azizov', 24, 'MALE', '+998904314123'),
('Angela', 'Merkel', 69, 'FEMALE', '+944119998877'),
('Qudrat', 'Rustamov', 26, 'MALE', '+998984324355'),
('Nodirjon', 'Quvvatov', 18, 'MALE', '+998994314534');

SELECT *FROM student;       

INSERT INTO student (first_name, second_name, age, gender) 
VALUES 
('Bolta', 'Teshaev', 35, 'MALE');

--jadvalni bo'shatish.
TRUNCATE TABLE student;  

SELECT id, first_name FROM student;

SELECT first_name AS ism, second_name AS sharif 
FROM student;

-- WHERE - QAYERDA ||| IF ga o'hshaydi. shart beriladi. > < >= <= = != <> (IS, OR, AND).
SELECT * 
FROM student 
WHERE gender = "MALE";

SELECT * 
FROM student 
WHERE first_name = "aziz";

SELECT * 
FROM student 
WHERE first_name != 'aziz';

SELECT * 
FROM student 
WHERE age > 20;

SELECT * 
FROM student 
WHERE phone_number = NULL;

SELECT * 
FROM student 
WHERE phone_number IS NULL;

--OR AND
SELECT * 
FROM student 
WHERE age <= 22 AND gender = 'Female';

SELECT * 
FROM student 
WHERE age <= 20 OR gender = 'FEMALE';

SELECT * 
FROM student 
WHERE 22 < age AND age < 27;


-- BETWEEN - ORASIDA
SELECT * 
FROM student 
WHERE age BETWEEN 22 AND 27;

SELECT * 
FROM student 
WHERE age NOT BETWEEN 22 AND 27;

SELECT * 
FROM student 
WHERE id BETWEEN 10 AND 25;

--ORDER BY sortlash. (ASC - o'sish tartibida, DESC - kamayish tartibida)
SELECT * 
FROM student 
ORDER BY age;

SELECT first_name, second_name 
FROM student 
ORDER BY first_name;

SELECT first_name, second_name, age 
FROM student 
ORDER BY first_name, age;

SELECT first_name, second_name, age 
FROM student 
ORDER BY first_name ASC;

SELECT first_name, second_name, age 
FROM student 
ORDER BY first_name DESC;

SELECT * 
FROM student 
ORDER BY first_name DESC;

--LIMIT - CHEGARA ||| offset,count.
SELECT *
FROM student 
LIMIT 5;

SELECT *
FROM student 
LIMIT 10,5;

SELECT *
FROM student 
ORDER BY first_name DESC 
LIMIT 5;

SELECT * 
FROM student 
WHERE gender = "Male" 
LIMIT 5; 

SELECT * 
FROM student 
WHERE 20 < age AND age <= 30 
LIMIT 5; 

--LIKE - O'XSHASH
SELECT * 
FROM student 
WHERE first_name LIKE "Aziz";

SELECT * 
FROM student 
WHERE first_name LIKE "Jon";

SELECT * 
FROM student 
WHERE first_name LIKE "%Jon";

SELECT * 
FROM student 
WHERE first_name LIKE "%ir%";

SELECT * 
FROM student 
WHERE second_name LIKE "__ov";

SELECT * 
FROM student 
WHERE second_name LIKE "K____ov";

SELECT * 
FROM student 
WHERE phone_number LIKE "+99890%";

SELECT *  FROM student  
WHERE phone_number 
LIKE "+99890%" or phone_number LIKE "+99897%";


SELECT * 
FROM student 
WHERE phone_number NOT LIKE "+99892%";

--IN - ICHIDA ||| ichida bo'lsa ko'rsatadi.
SELECT * 
FROM student 
WHERE first_name IN ('Jackie', 'Angela', 'Burgutali');

SELECT * 
FROM student 
WHERE first_name NOT IN ('Aziz', 'Aziza', 'Jan-Clod');

SELECT * 
FROM student 
WHERE age IN (20,25,63);

--Function SUM, AVG, MIN, MAX, COUNT
SELECT SUM(age) 
FROM student;

SELECT SUM(age) 
FROM student
WHERE age < 30;

SELECT SUM(age) 
FROM student
WHERE gender = 'FEMALE';

SELECT AVG(age) 
FROM student;

SELECT AVG(age) as ortacha_yosh 
FROM student;

SELECT MIN(age) 
FROM student;

SELECT MIN(first_name) 
FROM student;

SELECT MAX(age) 
FROM student;

SELECT MAX(age) 
FROM student
WHERE gender = 'MALE';

SELECT COUNT(*) 
FROM student;


SELECT COUNT(*) 
FROM student 
WHERE age > 25;

SELECT COUNT(DISTINCT age) 
FROM student;

SELECT age
FROM student
ORDER BY age;

SELECT COUNT(DISTINCT gender) 
FROM student;

SELECT COUNT(*) 
FROM student 
WHERE gender="Male";

SELECT COUNT(*) FROM student   
GROUP BY age   
HAVING COUNT(*)>=1;  

SELECT first_name, 2023 - age AS year 
FROM student;

SELECT first_name, 2023 - age AS year 
FROM student 
ORDER BY age;

--jadvalga yangi field qo'shish.
ALTER TABLE student 
ADD Email VARCHAR(255);

--jadvaldan fieldni o'chirish.
ALTER TABLE student 
DROP COLUMN Email;

ALTER TABLE student 
ADD DateOfBirth date; 

INSERT INTO student (first_name, second_name, age, gender, phone_number, DateOfBirth) 
VALUES 
('Bexruz', 'Rahimov', 15, 'MALE', '+99890775566', '2001-01-31');

ALTER TABLE student 
MODIFY COLUMN DateOfBirth YEAR; 

--UPDATE - YANGILASH
UPDATE student 
SET DateOfBirth = NULL
WHERE first_name = 'BEXRUZ';

UPDATE student 
SET age = 23 
WHERE first_name = 'Malika';

UPDATE student 
SET DateOfBirth = 2023 - age;

--DELETE - O'CHIRISH

DELETE FROM student 
WHERE age = 22;  

DELETE FROM student 
WHERE first_name = 'AZiz';

INSERT INTO student (id, first_name, second_name, age, gender, phone_number) VALUES
(99,'Gayrat', 'Bahromov', 31, 'MALE', '+998924324362');
