DROP DATABASE chatdb;
CREATE DATABASE chatdb;

USE chatdb;

CREATE TABLE IF NOT EXISTS user (  
    id SERIAL,  
    full_name VARCHAR(32) NOT NULL,  
    user_name VARCHAR(32) NOT NULL,  
    password VARCHAR(32) NOT NULL,  
    mobile_number VARCHAR(13) NOT NULL
);

INSERT INTO user (full_name, user_name, password, mobile_number) VALUES (
    'Aziz Shakirov', 'azizDoctor', 'qwerty', '+998977032636'
);

SELECT * FROM user;

SELECT * FROM user WHERE id = 1;


-- todo update user by id
UPDATE user SET full_name = 'Sardor', user_name = 'dr.Sardor', password = '1234567', mobile_number = '+998977771122' WHERE id = 1;


-- todo delete user by id
DELETE FROM user 
WHERE id = 1;

INSERT INTO user (full_name, user_name, password, mobile_number) VALUES (
    'Bekzod', 'bekKiller', '123456', '+998977442636'
);








insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-8', 'toyota', '1', '2');
insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'toyota', '0', '2');
insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'toyota', '0', '1');
insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-8', 'honda', '1', '2');
insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-8', 'honda', '2', '1');
insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'honda', '0', '1');
insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'honda', '1', '2');
insert into DailySales (date_id, make_name, lead_id, partner_id) values ('2020-12-7', 'honda', '2', '1');
