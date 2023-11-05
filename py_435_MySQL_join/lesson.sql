-- 175. Combine Two Tables
CREATE DATABASE IF NOT EXISTS Combine_Two_Tables;
USE Combine_Two_Tables;
CREATE TABLE IF NOT EXISTS Person (
    personId INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    lastName VARCHAR(32),
    firstName VARCHAR(32)
);

INSERT INTO Person(lastName, firstName) 
VALUES (Wang, Allen),(Alice, Bob);

CREATE TABLE IF NOT EXISTS Addres (
    addresId INT,
    personId INT, FOREIGN KEY(personId) REFERENCES Person(personId)
    city VARCHAR(64),
    state VARCHAR(64)
);

INSERT INTO Addres (
    city, state
);