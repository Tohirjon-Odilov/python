CREATE DATABASE homeworkdb;
DROP DATABASE homeworkdb;

USE homeworkdb;

DROP TABLE computer;

CREATE TABLE IF NOT EXISTS computer (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,  
    brand VARCHAR(32),
    model VARCHAR(32),
    cpu VARCHAR(32),
    frequency FLOAT(3,1), 
    ram INT,
    os VARCHAR(32),
    price DECIMAL(6,2) DEFAULT 0 
); 

INSERT INTO computer (brand, model, cpu, frequency, ram, os, price) VALUES 
('Apple', 'MacBook Pro', 'M2', 3.9, 16, 'MacOS', 1200),
('HP', 'All-in-One', 'Intel Core i3', 2.6, 8, 'Windows 11 Home', 455.2),
('Lenovo', 'IdeaCentre AIO', 'AMD Ryzen 5 5500U', 2.1, 8, 'Windows 10 Home', 431.2),
('Aser', 'Varition', 'Core i3 6th Gen', 1.8, 8, 'Windows 10', 245.5),
('ASUS', 'Vivo AiO V222', 'Intel Core i5-10210U 10th Gen', 3.4, 16, 'Windows 11 Home', 767.2),
('Apple', 'MacBook Air', 'M1', 2.5, 8, 'MacOS', 915.35),
('HP', 'OMEN', 'Intel Core i5', 3.6, 16, 'Windows 11 Home', 1455.2),
('Lenovo', 'Chromebook Duet 3', 'AMD Ryzen 4 3500U', 1.9, 2, 'Windows 10', 311.5),
('Aser', 'Nitro 5', 'Core i3 6th', 1.8, 4, 'Windows 9', 212.5),
('ASUS', 'ZenBook', 'Intel Core i7-12210U 12th Gen', 4.4, 16, 'Windows 11 Home', 1650.65);

INSERT INTO computer (brand, model, cpu, frequency, ram, os) VALUES 
('ASUS', 'Vivo AiO V111', 'Intel Core i5-10210U 10th Gen', 1.4, 16, 'Windows 11 Home'); 

INSERT INTO computer (brand, model, cpu, frequency, ram, os, price) VALUES 
('ASUS', 'Vivo AiO V111', 'Intel Core i5-10210U 10th Gen', 1.4, 16, 'Windows 11 Home', 456.126); 

-- jadvalni to'ldirish. 2 - usul. ko'p qatorli.
INSERT INTO computer (brand,model,cpu,frequency,ram,os,price) VALUES

("Apple",'MacBook Pro','Intel Core i7',2.6,16,'macOS 11 Big Sur',2399),
("Apple",'MacBook Air','M1',3.2,8,'macOS 11 Big Sur',999),
("Asus",'ZenBook Flip S','Intel Core i7',3.9,16,'Windows 10',400),
("Asus",'ROG Strix G15','AMD Ryzen 5',2.1,8,'Windows 10',1199),
("Dell",'XPS 13','Intel Core i5',2.3,8,'Ubuntu 20.04',1099),
("Dell",'G5 15','Intel Core i7',2.6,16,'Windows 10',1499),
("HP",'Spectre x360','Intel Core i7',2.8,16,'Windows 10',420),
("HP",'Pavilion Gaming','AMD Ryzen 5',2.0,8,'Windows 10',899),
("Lenovo","ThinkPad X1 Carbon",'Intel Core i7',2.7,16,'Windows 10',570),
("Lenovo","Yoga C740",'Intel Core i5',1.6,8,'Windows 10',1000),
("Microsoft",'Surface Book 3','Intel Core i7',2.3,16,'Windows 10',2299),
("Microsoft",'Surface Laptop 4','AMD Ryzen 5',2.0,8,'Windows 10',1299),
("Acer",'Swift 3','AMD Ryzen 5',2.0,8,'Windows 10',699),
("Acer",'Predator Helios 300','Intel Core i7',2.6,16,'Windows 10',1499),
("Razer",'Blade 15','Intel Core i7',2.6,16,'Windows 10',1000),
("MSI",'Prestige 14','Intel Core i5',1.6,16,'Windows 10',1299),
("Gigabyte",'AORUS 15G','Intel Core i7',2.6,16,'Windows 10',2199),
("Huawei ",'MateBook X Pro','Intel Core i7',2.8,16,'Windows 10',1699),
("LG",'Gram 17','Intel Core i7',2.3,16,'Windows 10',400),
("Samsung",'Galaxy Book Pro','Intel Core i7',2.8,16,'Windows 10',1799);

SELECT *
FROM computer 
ORDER BY price DESC
LIMIT 1;

SELECT * 
FROM computer
WHERE price = (SELECT MAX(price) FROM computer);

SELECT * 
FROM computer
WHERE price = (SELECT MIN(price) FROM computer);

SELECT frequency
FROM computer
WHERE price BETWEEN 400 AND 1000
AND cpu LIKE '%intel%';


SELECT COUNT(id)
FROM computer
WHERE brand = 'Apple';


SELECT *
FROM computer
WHERE brand = 'ASUS' AND
os LIKE '%Windows%' AND ram = 16
ORDER BY price;













SELECT *
FROM computer
WHERE ram = 8 AND brand = 'ASUS'
LIKE os '%Windows%'
ORDER BY price;

SELECT * 
FROM computer 
ORDER BY price DESC 
LIMIT 1;

SELECT * 
FROM computer 
ORDER BY price 
LIMIT 1;

SELECT frequency 
FROM computer 
WHERE price BETWEEN 400 AND 1000 
AND cpu LIKE '%intel%';

SELECT COUNT(brand)
FROM computer 
WHERE brand = "Apple";

SELECT *
FROM computer
WHERE ram = 8 AND brand = 'ASUS' 
AND os LIKE '%Windows%'
ORDER BY price;




CREATE DATABASE universitydb;

USE universitydb;

CREATE TABLE talaba ( 
    id INT NOT NULL AUTO_INCREMENT, 
    talaba_ismi VARCHAR(32) NOT NULL,
    talaba_kursi INT NOT NULL, 
    talaba_stependiyasi FLOAT,
    PRIMARY KEY (id) 
);

INSERT INTO talaba (talaba_ismi,talaba_kursi,talaba_stependiyasi) VALUES
    ('Ahadulla',1,540000),
    ('Javohor',3,540000),
    ('Ozod',1,540000),
    ('Behruz',2,540000),
    ('Muhammadali',2,540000),
    ('Xaytali',3,540000),
    ('Bobur',3,540000),
    ('Temur',2,540000),
    ('Azamat',1,450000.4),
    ('Ahmad',2,515000.5),
    ('Shokir',3,540000.1),
    ('Izzat',3,658000.0),
    ('Aziz',4,1658000.0),
    ('Murod',4,168000.0);


DELETE FROM talaba
WHERE talaba_kursi = 4;


UPDATE talaba 
SET talaba_kursi = talaba_kursi + 1;


















DELETE FROM talaba
WHERE talaba_kursi = 4;

UPDATE talaba
SET talaba_kursi = talaba_kursi + 1;

SELECT COUNT(*) FROM talaba WHERE talaba_kursi = 1;
SELECT COUNT(*) FROM talaba WHERE talaba_kursi = 2;
SELECT COUNT(*) FROM talaba WHERE talaba_kursi = 3;
SELECT COUNT(*) FROM talaba WHERE talaba_kursi = 4;

SELECT talaba_kursi, count(talaba_kursi) from talaba group by(talaba_kursi) order by talaba_kursi;

select talaba_kursi, sum(talaba_stependiyasi) from talaba group by talaba_kursi having sum(talaba_stependiyasi) > 2000000;

SELECT talaba_kursi, sum(talaba_stependiyasi) from talaba group by(talaba_kursi) having sum(talaba_stependiyasi) > 2000000 order by sum(talaba_st
ependiyasi);

CREATE TABLE ovqat ( 
id INT NOT NULL AUTO_INCREMENT,
taom_nomi VARCHAR(32) NOT NULL,
taom_masalliqlari TEXT,
PRIMARY KEY (id)
);

INSERT INTO ovqat(taom_nomi,taom_masalliqlari) VALUES
    ('Osh',"go'sh , piyoz, sabzi, guruch, yog'"),
    ('Mastava', "yog', kartoshka, sabzi, piyoz, guruch"),
    ('Somsa',"un, go'sh, piyoz"),
    ('Manti', "un, go'sh, piyoz"),
    ('Xonim', "un, go'sh, piyoz, saryog'"),
    ("Shorva", "go'sh , piyoz, sabzi, kartoshka, pomidor"),
    ('Sumalak', "bug'doy, un, yog'"),
    ('Shovla',"go'sh , piyoz, sabzi, guruch, yog'"),
    ('Moshxorda',"go'sh , piyoz, sabzi, kartoshka, pomidor, mosh"),
    ('Shulla', "qatiq, guruch");

SELECT *
FROM ovqat
WHERE taom_nomi LIKE "%a";

SELECT *
FROM ovqat
WHERE taom_masalliqlari LIKE "%guruch%";
