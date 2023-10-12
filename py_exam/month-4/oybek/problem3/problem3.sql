CREATE DATABASE UZAIRLENS;

USE UZAIRLENS;

CREATE TABLE airport (
    id SERIAL,
    flight VARCHAR(10),
    departure VARCHAR(64),
    arrive VARCHAR(64),
    day INT,
    month INT,
    year INT
);

INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb92358', 'TOSHKENT', 'ISTANBUL', 6, 5, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb92373', 'TOSHKENT', 'BERLIN', 22, 8, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb92393', 'FARGONA', 'MELBURN', 11, 9, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb92322', 'TOSHKENT', 'NEW YORK', 16, 7, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb94347', 'TOSHKENT', 'PARIJ', 1, 12, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb92331', 'FARGONA', 'BERLIN', 1, 8, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb94352', 'TOSHKENT', 'ANQARA', 2, 10, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb95323', 'FARGONA', 'BRIGHTON', 5, 9, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb95354', 'TOSHKENT', 'LONDON', 4, 3, 2023);
INSERT INTO airport (flight, departure, arrive, day, month, year) VALUES ('uzb95387', 'TOSHKENT', 'FARGONA', 26, 8, 2023);

SELECT * FROM airport WHERE ARRIVE='BERLIN' AND month=8;

SELECT * FROM airport WHERE month=9;

SELECT * FROM airport WHERE day<16 AND month<7;