CREATE DATABASE najottalimdb;

USE najottalimdb;

    CREATE TABLE IF NOT EXISTS course (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
        name VARCHAR(64) UNIQUE
    );


    INSERT INTO course (name) VALUES 
    ('NodeJS'),
    ('.NET'),
    ('Java'),
    ('Frontend'),
    ('Go'),
    ('FLATTER'),
    ('PHP'),
    ('Fullstack');

CREATE TABLE IF NOT EXISTS student (
    id SERIAL, -- BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
    first_name VARCHAR(32),
    course_id INT, FOREIGN KEY(course_id) REFERENCES course(id)
);

INSERT INTO student (first_name, course_id) VALUES
('Azizabonu', 8),
('Dilshodbek', 2),
('Akromjon', 5),
('Saidislom', 8),
('Ahrorbek', 5),
('Bobomurod', 5),
('Samiya', 4),
('Intizor', 2),
('Dilfuza', 5),
('Asadbek', 7),
('Muzaffar', 5),
('Akobir', 8),
('Toxirjon', 2),
('Nasiba', 4),
('Akmalxoja', NULL),
('Muhammadsodiq', 2),
('Aziz', NULL);

select * from student inner join course  on course_id = course.id;
select first_name as 'First name', name as 'Course name' from student inner join course as c on course_id = c.id;
select first_name as 'First name', name as 'Course name' from student left join course as c on course_id = c.id;
select * from student left join course as c on course_id = c.id;
select * from course as c RIGHT join student on course_id = c.id;
select first_name as 'First name', name as 'Course name' from course RIGHT join student as c on course_id = c.id;
select first_name as 'First name', name as 'Course name' from student RIGHT join course as c on course_id = c.id;



SELECT s.id, s.first_name, c.name as 'course name' FROM  course as c RIGHT JOIN student as s ON c.id = course_id;
SELECT s.id, s.first_name, c.name as 'course name' FROM  course as c LEFT JOIN student as s ON c.id = course_id;
SELECT s.id, s.first_name, c.name as 'course name' FROM  course as c JOIN student as s ON c.id = course_id;