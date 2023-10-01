-- w1

CREATE TABLE computers  
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR 60 NOT NULL,
    model VARCHAR 60 NOT NULL,
    cpu VARCHAR 60 NOT NULL,
    frequency DECIMAL 3, 1 CHECK  frequency >= 1.8 AND frequency <= 5.0,
    ram INT CHECK  ram IN  2, 4, 8, 16,
    os VARCHAR 20 NOT NULL,
    price DECIMAL 6, 2 CHECK  price >= 400 AND price <= 3000;


-- 1. Ma'lumotlar bazasini 20 ta ma'lumot bilan to'ldirish
INSERT INTO computers (brand, model, cpu, frequency, ram, os, price)
VALUES
    ('Apple', 'MacBook Pro', 'Intel Core i7', 2.5, 8, 'macOS', 1999.99),
    ('ASUS', 'ZenBook', 'Intel Core i5', 1.8, 8, 'Windows 10', 899.99),
    ('HP', 'Pavilion', 'AMD Ryzen 5', 2.3, 16, 'Windows 11', 1249.99),
    ('Dell', 'XPS', 'Intel Core i7', 3.1, 16, 'Ubuntu 20.04', 1599.99),
    ('Lenovo', 'ThinkPad', 'Intel Core i5', 2.0, 8, 'Windows 10', 1099.99),
    ('Acer', 'Predator', 'AMD Ryzen 7', 2.8, 16, 'Windows 10', 1399.99),
    ('MSI', 'GS66', 'Intel Core i9', 2.9, 32, 'Windows 11', 2199.99),
    ('Alienware', 'M17 R4', 'Intel Core i7', 2.6, 16, 'Windows 10', 1799.99),
    ('Razer', 'Blade 15', 'Intel Core i7', 2.4, 16, 'Windows 11', 1899.99),
    ('Microsoft', 'Surface Laptop 4', 'AMD Ryzen 7', 2.3, 16, 'Windows 10', 1499.99),
    ('LG', 'Gram', 'Intel Core i5', 2.0, 16, 'Windows 11', 1299.99),
    ('Sony', 'VAIO', 'Intel Core i5', 1.9, 8, 'Windows 10', 999.99),
    ('Samsung', 'Galaxy Book', 'Intel Core i7', 2.4, 16, 'Windows 11', 1699.99),
    ('Toshiba', 'Satellite', 'Intel Core i3', 1.7, 4, 'Windows 10', 799.99),
    ('Fujitsu', 'Lifebook', 'Intel Core i7', 2.2, 16, 'Windows 10', 1299.99),
    ('Huawei', 'MateBook', 'AMD Ryzen 5', 2.0, 8, 'Windows 10', 899.99),
    ('Xiaomi', 'Mi Notebook', 'Intel Core i5', 2.2, 8, 'Windows 11', 999.99),
    ('Google', 'Pixelbook', 'Intel Core i5', 1.9, 8, 'Windows 7', 1199.99),
    ('Acer', 'Chromebook', 'Intel Celeron', 1.1, 4, 'Windows 8', 499.99),
    ('ASUS', 'Chromebook', 'Intel Pentium', 1.2, 4, 'Kali purple', 549.99);

-- 2. Har bir <brand>dan kamida 2 ta qaytarilishi shart
SELECT brand, COUNT(*) AS brand_count
FROM computers
GROUP BY brand
HAVING brand_count >= 2;

-- 3. <cpu> kamida 2 marta qaytarilishi shart
SELECT cpu, COUNT(*) AS cpu_count
FROM computers
GROUP BY cpu
HAVING cpu_count >= 2;


SELECT * FROM computers ORDER BY price DESC LIMIT 1;

SELECT * FROM computers ORDER BY price ASC LIMIT 1;

SELECT frequency FROM computers WHERE price BETWEEN 400 AND 1000 AND cpu LIKE '%Intel%';

SELECT COUNT(*) AS brand_count FROM computers WHERE brand = 'Apple';

SELECT * FROM computers WHERE os Like 'Windows%' AND ram = 8 AND brand = 'ASUS' ORDER BY price;




-- w2

-- Ma'lumotlar bazasini yaratish
CREATE DATABASE UNIVERSITET;
USE UNIVERSITET;

-- Talaba nomli jadvalni yaratish
CREATE TABLE talaba (
    id INT AUTO_INCREMENT PRIMARY KEY,
    talaba_ismi VARCHAR(255) NOT NULL,
    talaba_kursi INT NOT NULL,
    talaba_stipendiyasi DECIMAL(8, 2) NOT NULL
);

-- 10 ta ma'lumotni qo'shish
INSERT INTO talaba (talaba_ismi, talaba_kursi, talaba_stipendiyasi) VALUES
    ('Talaba1', 1, 500.00),
    ('Talaba2', 2, 600.00),
    ('Talaba3', 1, 450.00),
    ('Talaba4', 3, 700.00),
    ('Talaba5', 4, 750.00),
    ('Talaba6', 1, 500.00),
    ('Talaba7', 2, 600.00),
    ('Talaba8', 3, 700.00),
    ('Talaba9', 1, 450.00),
    ('Talaba10', 4, 750.00);

-- 1-so'rov: Barcha talabalar kursini 1taga oshiring va 4-kurslarni o'chirib tashlang
UPDATE talaba SET talaba_kursi = talaba_kursi + 1 WHERE talaba_kursi < 4;
DELETE FROM talaba WHERE talaba_kursi = 4;

-- 2-so'rov: Har bir kursda nechta talabalar o'qishini aniqlash va chiqarish
SELECT talaba_kursi, COUNT(*) AS talabalar_soni FROM talaba GROUP BY talaba_kursi;




-- w3

-- Ma'lumotlar bazasini yaratish
CREATE DATABASE MILLIY_TAOMLAR;
USE MILLIY_TAOMLAR;

-- Ovqat nomli jadvalni yaratish
CREATE TABLE ovqat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    taom_nomi VARCHAR(255) NOT NULL,
    taom_masaliqlari TEXT
);

-- 10 ta ma'lumotni qo'shish
INSERT INTO ovqat (taom_nomi, taom_masaliqlari) VALUES
    ("Manti", "Go'sht, un, tuz, piyoz"),
    ("Lag`mon", "Go'sht, pomidor, piyoz, sabzi, piyoz, ziravorlar"),
    ("Somsa", "Go'sht, un, tuz, piyoz"),
    ("Shashlik", "Go'sht, piyoz, sabzi"),
    ("Palov", "Go'sht, bug`doy, piyoz, mosh, guruch"),
    ("Dimlama", "Go'sht, sabzi, piyoz, mosh"),
    ("Sho'rva", "Go'sht, sabzavotlar, piyoz"),
    ("Mastava", "Go'sht, piyoz, mosh, guruch, sabzi"),
    ("Grechka", "Go'sht, piyoz, grechka, sabzi, kartoshka, zira"),
    ("Norin", "Un, go'sht, piyoz, sabzavotlar");


-- 1-so'rovda taom_nomi a harfi bilan tugagan ovqatlarni chiqaring.
SELECT * FROM ovqat WHERE taom_nomi LIKE '%a';


-- 2-so'rovda masaliqlarida guruch qatnashgan ovqatlarni chiqaring.
SELECT * FROM ovqat WHERE taom_masaliqlari LIKE "%guruch%"