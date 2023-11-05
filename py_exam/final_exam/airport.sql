USE Exam;
CREATE TABLE flights(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    flight VARCHAR(10),
    departure VARCHAR(64),
    arrive VARCHAR(64),
    day INTEGER,
    month INTEGER,
    year INTEGER
);

INSERT INTO flights (flight, departure, arrive, day, month, year)
VALUES
    ('HY123', 'Tashkent', 'Istanbul', 15, 01, 2023),
    ('TK456', 'Istanbul', 'New York', 20, 04, 2023),
    ('LH789', 'New York', 'Berlin', 25, 08, 2023),
    ('AF234', 'Berlin', 'Paris', 30, 10, 2023),
    ('EK567', 'Paris', 'Dubai', 5, 09, 2023),
    ('QR890', 'Dubai', 'Doha', 10, 11, 2023),
    ('SU123', 'Doha', 'Moscow', 15, 09, 2023),
    ('BA456', 'Moscow', 'London', 05, 01, 2023),
    ('AF789', 'London', 'Paris', 12, 01, 2023),
    ('TK234', 'Paris', 'Istanbul', 30, 09, 2023);

SELECT * FROM flights
WHERE arrive = "Berlin" and month = 08;

SELECT * FROM flights
WHERE month = 09;

SELECT * FROM flights
WHERE month = 1 AND day <= 15;
