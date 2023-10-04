CREATE DATABASE Avtosalon;
USE Avtosalon;
CREATE TABLE cars(
    name VARCHAR(15),
    price INT,
    capacity DECIMAL,
    color VARCHAR(20),
    warranty INT
);
SHOW TABLES;
DESC cars;
INSERT INTO cars VALUES 
('Toyota', 1500, 100, 'red', 10),
('Mercedes', 2000, 100, 'black', 10),
('BMW', 2500, 100, 'white', 10),
('Lada', 1000, 100, 'white', 10),   
("Malibu", 1200, 100, 'red', 10),
("Ford", 1300, 100, 'white', 10),
("Porsche", 3000, 100, 'black', 10),
("Audi", 4000, 100, 'white', 10),
("Lexus", 5000, 100, 'black', 10),
("Bentley", 6000, 100, 'white', 10),
('Malibu', 40000, 70, 'oq', '8'),
('Kobalt', 15000, 60, 'oq', '8'),
('Kobalt', 13000, 60, 'kulrang', '8'),
('Gentra', 17000, 70, 'qora', '9'),
('BYD', 45000, 95, 'qizil', '5'),
('BMW', 65000, 85, 'oq', '15'),
('nexiya', 8000, 55, 'sariq', '5'),
('BYD', 48000, 95, 'qora', '8'),
('Epica', 15000, 65, 'oq', '5'),
('Tahoe', 100000, 100, 'qora', '10');

------------- ! W8 ---------------

-- 4.
UPDATE cars 
SET price = 3020 
WHERE price > 1000 AND price < 2000;

-- 5.
UPDATE cars
SET capacity = 200
WHERE warranty = 1;

-- 6.
ALTER TABLE cars
ADD quality TEXT;

-- 7.
UPDATE cars
SET quality = "premium"
WHERE price = (SELECT max(price) FROM cars);

-- 8.
UPDATE cars
SET quality = 'low'
WHERE price = (SELECT MIN(price) FROM cars);

-- 9.
ALTER TABLE cars
MODIFY COLUMN quality TEXT AFTER name;

-- 10.
SELECT name "ismi", price "narxi", capacity "sig'imi", color "rangi", warranty "garantiyasi", quality "sifati" FROM cars


------------- ! W9 ---------------
CREATE DATABASE School;
USE School;
CREATE TABLE teachers (
    name varchar(50),
    surname varchar(50),
    salary int,
    experience int,
    branch varchar(50)
);

INSERT INTO teachers VALUES
("Ahmad", "Xoliqov", 1200, 2, "Chilonzor"),
("Aziz", "Shakirov", 2000, 5, "Chilonzor"),
("Nurzat", "Husanov", 1500, 3, "Chimboy"),
("Bekzat", "Xoliqov", 1300, 4, "Xadra"),
("Jasur", "Xoliqov", 1100, 1, "Farg'ona"),
("Rahim", "Xoliqov", 1000, 1, "Farg'ona"),
("Sardor", "Xoliqov", 1100, 1, "Farg'ona"),
("Nurzat", "Husanov", 1500, 3, "Chimboy");

CREATE TABLE students(
    name varchar(50),
    surname varchar(50),
    monthly_payment int,
    course_duration int,
    branch varchar(50)
);

INSERT INTO students VALUES
("Tohirjon", "Odilov", 2200, 11, "Chilonzor"),
("Asadbek", "Faxriddinov", 3200, 11, "Chilonzor"),
("Akramjon", "Abduvahobov", 2200, 12, "Farg'ona"),
("Ahrorbek", "Alijonov", 2200, 12, "Farg'ona"),
("Jasur", "Hamdamov", 1200, 12, "Farg'ona"),
("Bobomurod", "Artiqaliyev", 3000, 10, "Xadra"),
("Sardor", "Xoliqov", 1100, 1, "Farg'ona"),
("Nurzat", "Husanov", 1500, 3, "Chimboy");

-- 1.
SELECT * FROM teachers ORDER BY salary;

-- 9.
-- SELECT students.name, students.branch, teachers.name, teachers.branch FROM students

-- JOIN teachers ON teachers.branch = students.branch;
-- ORDER BY students.name;

