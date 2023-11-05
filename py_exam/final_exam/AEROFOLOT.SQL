CREATE TABLE AEOROFLOT(
    id INTEGER AUTO_INCREMENT PRIMARY KEY, 
    type VARCHAR(17), 
    trip INTEGER,
    town_from VARCHAR(30),
    town_to VARCHAR(30),
    time VARCHAR(8)
);

INSERT INTO AEOROFLOT(type, trip, town_from, town_to, time) VALUES
    ("Boing747", 25, "GER", "UK", '14:30:00'),
    ("Airbus A330", 30, "UK", "GER", '10:30:00'),
    ("Embraer E190", 15, "USA", "FR", '16:30:00'),
    ("Boing737", 20, "RUS", "UZB", '18:00:00'),
    ("Airbus A320", 40, "CHINA", "UZB", '06:00:00'),
    ("Airbus A380", 35, "FRA", "UZB", '09:30:00'),
    ("Boing787", 19, "UK", "UZB", '05:30:00'),
    ("Airbus A350", 28, "USA", "CHINA", '19:30:00'),
    ("Embraer E195", 22, "GER", "RUS", '15:30:00'),
    ("Boing767", 17, "USA", "UZB", '08:00:00');

SELECT * from AEOROFLOT ORDER BY time ASC LIMIT 1;

SELECT *
FROM AEOROFLOT
ORDER BY trip DESC
LIMIT 3;