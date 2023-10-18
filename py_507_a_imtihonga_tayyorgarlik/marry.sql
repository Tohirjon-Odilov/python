CREATE DATABASE Exam;
USE Exam;
CREATE TABLE User (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    name CHAR(20),
    surname CHAR(20),
    age INTEGER,
    address text
);

INSERT INTO User(name, surname, age, address) VALUES
    ("Abdulla", "Abdullayev", 25, "Toshkent sh., M.Ulug'bek tumani, Bobur ko'chasi 5-uy"),
    ("Nodira", "Abdullayeva", 22, "Toshkent sh., M.Ulug'bek tumani, Bobur ko'chasi 5-uy"),
    ("Hilola", "Rasulova", 21, "Toshkent sh., Chilonzor tumani, Jalilov ko'chasi 5-uy 2-honadon"),
    ("Jalil", "Rasulov", 18, "Toshkent sh., Chilonzor tumani, Jalilov ko'chasi 5-uy 2-honadon"),
    ("Sardor","Kamolov", 20, "Toshkent sh., Yashnabod tumani, 2-kvartal, 4-uy 75-honadon"),
    ("Lola","Kamolova", 24, "Toshkent sh., Yashnabod tumani, 2-kvartal, 4-uy 75-honadon"),
    ("Shoxrux", "Rustamov", 20, "Toshkent sh., Chilonzor tumani, Namatak ko'chasi 1-uy 25-honadon"),
    ("Temur","Qodirov", 23, "Toshkent sh., Yashnabod tumani, Safiya ko'chasi, 25-uy"),
    ("Botir","Malikov", 19, "Toshkent sh., Mirobod tumani, Temuriylar ko'chasi, 12-uy"),
    ("Maftuna","Farruxova", 19, "Toshkent sh., Olmazor tumani, Amir Temur ko'chasi, 4-uy 63-honadon");

select * from User
GROUP BY address
HAVING COUNT(address) >= 2;

select * from User
GROUP BY address
HAVING COUNT(address) = 1;