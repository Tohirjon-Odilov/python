DROP DATABASE najottalimdb; 

CREATE DATABASE najottalimdb2;

USE najottalimdb2;

CREATE TABLE IF NOT EXISTS course (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(64) UNIQUE
);

CREATE TABLE IF NOT EXISTS student (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(32),
    last_name VARCHAR(32),
    date_of_birth DATE
);

CREATE TABLE IF NOT EXISTS it_center (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    student_id INT, FOREIGN KEY(student_id) REFERENCES student(id),
    course_id INT, FOREIGN KEY(course_id) REFERENCES course(id)
);

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


INSERT INTO student (first_name, last_name, date_of_birth) VALUES
    ('Fazliddin', 'Abbosov', '2000-01-05'),
    ('Hamid', 'Karimov', '1997-05-21'),
    ('Javlon', 'Payonov', '2005-09-11'),
    ('Komiljon', 'Allaniyozov', '2001-08-15'),
    ('Hadicha', 'Ibroximova', '1998-11-27'),
    ('Bekzod', 'Baxromov', '2003-03-18'),
    ('Yulduz', 'Mirbabaeva', '2002-07-25');


INSERT INTO it_center (student_id, course_id) VALUES
    (1,1), (1,2), (2,3), (3,4), (3,5), (4,2), (5,6), (6,7), (6,8);


SELECT * FROM student as s left join it_center as i on s.id = i.student_id left join course as c on c.id = i.course_id;


SELECT s.id, s.first_name, i.course_id
FROM student as s 
INNER JOIN it_center as i
ON s.id = i.student_id


SELECT *
FROM student as s 
INNER JOIN it_center as i
ON s.id = i.student_id
INNER JOIN course as c 
ON c.id = i.course_id;

SELECT s.id, s.first_name, c.name
FROM student as s 
INNER JOIN it_center as i
ON s.id = i.student_id
INNER JOIN course as c 
ON c.id = i.course_id;


SELECT s.id, CONCAT(s.first_name, ' ', s.last_name) as 'Full name', GROUP_CONCAT(c.name) as 'course names'
FROM student as s 
INNER JOIN it_center as i
ON s.id = i.student_id
INNER JOIN course as c 
ON c.id = i.course_id
GROUP BY s.id;


SELECT s.id, CONCAT(s.first_name, ' ', s.last_name) as 'Full name', GROUP_CONCAT(c.name) as 'course names'
FROM student as s 
LEFT JOIN it_center as i
ON s.id = i.student_id
LEFT JOIN course as c 
ON c.id = i.course_id
GROUP BY s.id;


SELECT s.id, first_name, i.course_id
FROM student as s
JOIN it_center as i
ON s.id = i.student_id; 

SELECT s.id, CONCAT(first_name,' ', last_name) as 'Full name' , GROUP_CONCAT(c.name) as 'courses names'
FROM student as s
JOIN it_center as i
ON s.id = i.student_id
JOIN course as c 
ON c.id = i.course_id
WHERE s.first_name = 'Fazliddin'
GROUP BY s.id
;



SELECT 
    ic.id as id, CONCAT(s.first_name,' ', s.last_name) as 'Full name', c.name as 'Course'
FROM
    it_center as ic
JOIN 
    student as s 
ON s.id = ic.student_id
JOIN
    course as c 
ON c.id = ic.course_id;
