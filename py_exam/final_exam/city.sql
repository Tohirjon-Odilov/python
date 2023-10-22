CREATE DATABASE city;
USE city;

CREATE TABLE city(
    id INTEGER AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(17), 
    country_code VARCHAR(3), 
    population INTEGER
);

INSERT INTO city (name, country_code, population) VALUES
    ('Ankara', 'TUR', 8600000),
    ('Tashkent', 'UZB', 3310000),
    ('Fergana', 'UZB', 230000),
    ('Baku', 'AZE', 1780000),
    ('Nassau', 'BHS', 322000),
    ('Tokio', 'CHN', 381000),
    ('Kingston', 'JAM', 117000),
    ('Berlin', 'BER', 117000),
    ('PUSAN', 'CHN', 117000),
    ('Spain', 'SPN', 112000);

SELECT COUNT(*) as "more",
(SELECT COUNT(*) FROM city WHERE population < 1000000) as "less"
FROM city
WHERE population > 1000000;

SELECT * FROM city WHERE country_code = 'UZB';
