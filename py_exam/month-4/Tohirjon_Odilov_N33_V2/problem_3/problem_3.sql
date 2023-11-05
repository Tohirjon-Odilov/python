CREATE DATABASE EXAM;
USE EXAM;

CREATE TABLE notebooks(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(128),
    cpu VARCHAR(64),
    frequency FLOAT,
    ram INTEGER,
    gpu INTEGER,
    price INTEGER
);

INSERT INTO notebooks(model, cpu, frequency, ram, gpu, price)
VALUES('Asus', 'Intel core i7', 3.2, 8, 4, 1200),
      ('DELL', 'AMD Rysen 9', 5.5, 32, 4, 1500),
      ('HP', 'Intel core i5', 2.2, 8, 1, 400),
      ('DELL', 'Intel core i7', 3.2, 16, 2, 450),
      ('MacBook', 'Intel core i7', 3.2, 16, 5, 2000),
      ('Asus', 'Intel core i7', 3.2, 8, 3, 1200),
      ('DELL', 'AMD Rysen 3', 3.2, 8, 3, 400),
      ('HP', 'Intel core i5', 3.2, 8, 4, 1000),
      ('Lenovo', 'Intel core i7', 3.2, 16, 2, 500),
      ('MacBook', 'Intel core i7', 3.2, 16, 6, 2000),
      ('Lenovo', 'Intel core i3', 3.2, 8, 1, 300);

-- 1
SELECT * FROM notebooks
WHERE model LIKE "%DELL%" AND price < 500;

-- 2
SELECT * FROM notebooks
WHERE ram > 8 AND gpu = 2;

-- 3
SELECT * FROM notebooks
WHERE cpu LIKE "%AMD%" AND frequency > 2;
