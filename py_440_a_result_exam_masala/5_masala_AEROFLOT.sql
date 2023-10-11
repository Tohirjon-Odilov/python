-- 5-masala. AEROFLOT
CREATE TABLE airplane(
    id INTEGER AUTO_INCREMENT PRIMARY KEY, --ID raqam
    type VARCHAR(17), -- Samolyot turi
    trip INTEGER, -- Reys raqami
    town_from VARCHAR(30), -- Uchish shaxri
    town_to VARCHAR(30), -- Qo'nish shaxri
    time VARCHAR(8) -- Uchish vaqti (soat:daqiqa:soniya)
);

INSERT airplane(type, trip, town_from, town_to, time)
VALUES('Boeing 737', 1, 'Toshkent', 'Tashkent', '10:00:00'),
      ('Boeing 737', 2, 'Toshkent', 'Dubai', '11:00:00'),
      ('Boeing 737', 3, 'Moskva', 'Amerka', '12:00:00'),
      ('Boeing 737', 4, 'Toshkent', 'Tashkent', '13:00:00'),
      ('Boeing 737', 5, 'Toshkent', 'Tashkent', '14:00:00'),
      ('Boeing 737', 6, 'Toshkent', 'Tashkent', '15:00:00'),
      ('Boeing 737', 7, 'Toshkent', 'Tashkent', '16:00:00'),
      ('Boeing 737', 8, 'Toshkent', 'Tashkent', '17:00:00'),
      ('Boeing 737', 9, 'Toshkent', 'Tashkent', '18:00:00'),
      ('Boeing 737', 10, 'Toshkent', 'Tashkent', '19:00:00'),
      ('Boeing 737', 11, 'Toshkent', 'Tashkent', '20:00:00');