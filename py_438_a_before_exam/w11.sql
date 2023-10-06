-- ? W11
CREATE DATABASE Lesson;
SHOW DATABASES;
USE Lesson;
CREATE TABLE Company(
    name VARCHAR(50),
    location VARCHAR(50),
    capital INT,
    employees_count INT,
    establishedAt INT,
    monthly_expenses INT
);
INSERT INTO Company
VALUES ('Amazon', 'Seattle', 200, 500, 2010, 1000),
    ('Facebook', 'New York', 300, 1000, 2011, 2000),
    ('Google', 'Tashkent', 500, 1500, 2012, 3000),
    ('Microsoft', 'Redmond', 200, 2000, 2013, 4000),
    ('Twitter', 'San Francisco', 500, 2500, 2014, 5000);
    
-- 1
SELECT *
FROM Company
ORDER BY name;

-- 2
SELECT *
FROM Company
ORDER BY capital DESC;

-- 3
SELECT *
FROM Company
WHERE employees_count = (
        SELECT MIN(employees_count)
        FROM Company
    );
    
-- 4
SELECT *
FROM Company
WHERE location = "Tashkent";

-- 5 
SELECT location,
    COUNT(*)
FROM Company
GROUP BY location;

-- 6
SELECT name, ((2023 - establishedAt) * 12) * monthly_expenses AS months_old
FROM Company;