CREATE TABLE AEOROFLOT(
    id INTEGER AUTO_INCREMENT PRIMARY KEY, 
    type VARCHAR(17), 
    trip INTEGER,
    town_from VARCHAR(30),
    town_to VARCHAR(30),
    time VARCHAR(8)
);

INSERT INTO AEOROFLOT(type, trip, town_from, town_to, time) VALUES
    ("Boing77", 12, "USA", "UZB", '12:30:00'),
    ("Boing77", 18, "UK", "UZB", '20:30:00'),
    ("Boing77", 101, "KZ", "FR", '06:30:00'),
    ("Boing77", 13, "USA", "AUS", '10:00:00'),
    ("Boing77", 159, "CHINA", "UZB", '08:00:00'),
    ("Boing77", 114, "USA", "UZB", '12:00:00'),
    ("Boing77", 184, "USA", "UZB", '12:00:00'),
    ("Boing77", 11, "USA", "CHINE", '22:00:00'),
    ("Boing77", 14, "UK", "UZB", '04:30:00'),
    ("Boing77", 10, "USA", "UZB", '13:00:00');