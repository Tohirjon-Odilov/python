CREATE DATABASE najottalimdb;

USE najottalimdb;

CREATE TABLE IF NOT EXISTS course (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(64) UNIQUE
);

SELECT s.id, first_name, last_name, name FROM student as s INNER JOIN course as c ON s.course_id = c.id;


INSERT INTO course (name) VALUES
    ('FullStack'),
    ('Grafik dizayn'),
    ('Foundation'),
    ('Go'),
    ('Frontend'),
    ('SMM'),
    ('English for IT'),
    ('QA'),
    ('Java');

CREATE TABLE IF NOT EXISTS student (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(32),
    last_name VARCHAR(32),
    date_of_birth DATE,
    course_id INT
);

INSERT INTO student (first_name, last_name, date_of_birth, course_id) VALUES
    ('Fazliddin', 'Abbosov', '2000-01-05', 1),
    ('Hamid', 'Karimov', '1997-05-21', 4),
    ('Javlon', 'Payonov', '2005-09-11', 5),
    ('Komiljon', 'Allaniyozov', '2001-08-15', 3),
    ('Hadicha', 'Ibroximova', '1998-11-27', 2),
    ('Bekzod', 'Baxromov', '2003-03-18', 1),
    ('Yulduz', 'Mirbabaeva', '2002-07-25', NULL);

SELECT *
FROM student as s
JOIN course as c
ON c.id = course_id;

SELECT s.id, first_name, c.name
FROM student as s
JOIN course as c
ON c.id = course_id;

SELECT s.id, first_name, c.name as 'course name'
FROM student as s
JOIN course as c
ON c.id = course_id;

SELECT s.id, CONCAT(first_name, ' ', last_name) as 'Full name', c.name as 'course name'
FROM student as s
JOIN course as c
ON c.id = course_id;

SELECT s.id, CONCAT(first_name, ' ', last_name) as 'Full name', c.name as 'course name'
FROM student as s
INNER JOIN course as c
ON c.id = course_id;

SELECT s.id, CONCAT(first_name, ' ', last_name) as 'Full name', c.name as 'course name'
FROM student as s
LEFT JOIN course as c
ON c.id = course_id;

SELECT s.id, CONCAT(first_name, ' ', last_name) as 'Full name', c.name as 'course name'
FROM student as s
RIGHT JOIN course as c
ON c.id = course_id;

SELECT s.id, CONCAT(first_name, ' ', last_name) as 'Full name', c.name as 'course name'
FROM student as s
CROSS JOIN course as c
ON c.id = course_id;















SELECT id, first_name 
FROM student
UNION
SELECT id, name
FROM course;


SELECT s.id, concat(first_name,' ', last_name) as 'full name', name as 'course name'
FROM student as s
JOIN course as c
ON c.id = course_id;

SELECT s.id, first_name, c.name
FROM student as s
LEFT JOIN course as c
ON c.id = course_id;

SELECT s.id, first_name, c.name
FROM student as s
RIGHT JOIN course as c
ON c.id = course_id;

SELECT s.id, first_name, c.name
FROM student as s
CROSS JOIN course as c
ON c.id = course_id;






















SELECT student.id, student.first_name, course.name
FROM student
INNER JOIN course ON student.course_id=course.id;

SELECT student.id, student.first_name, course.name    
FROM student  
INNER JOIN course    
USING (id);  

SELECT student.id, student.first_name, course.name
FROM student
LEFT JOIN course ON student.course_id=course.id;

SELECT student.id, student.first_name, course.name
FROM student
RIGHT JOIN course ON student.course_id=course.id;

SELECT *
FROM student
CROSS JOIN course;

SELECT s.id, s.first_name, s.last_name, c.name
FROM student as s
CROSS JOIN course as c
WHERE s.course_id=c.id;