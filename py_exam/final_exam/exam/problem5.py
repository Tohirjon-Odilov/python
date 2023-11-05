import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="exam"
)

# Cursor yaratish
# cursor = conn.cursor()

# Ma'lumotlarni kiritish
sql = """
create table employe1(
    EMPLOYEE_ID integer,
    FIRST_NAME varchar(50),
    LAST_NAME varchar(50),
    EMAIL varchar(50),
    PHONE_NUMBER varchar(50),
    HIRE_DATE date,
    JOB_ID varchar(50),
    SALARY integer,
    COMPRESSION_PCT FLOAT,
    MANAGER_ID integer,
    DEPARTMENT_ID integer
);


INSERT INTO employe1 VALUES 
    (1, 'Ism1', 'Familiya1', 'email1@example.com', '123456789', '2023-10-28', 'JOB1', 50000, 0.1, 2, 60),
    (2, 'Ism2', 'Familiya2', 'email2@example.com', '987654321', '2023-10-29', 'JOB2', 60000, 0.2, 3, 90),
    (3, 'Ism3', 'Familiya3', 'email3@example.com', '111111111', '2023-10-30', 'JOB3', 70000, 0.3, 4, 50),
    (4, 'Ism4', 'Familiya4', 'email4@example.com', '999999999', '2023-10-31', 'JOB4', 80000, 0.4, 5, 20),
    (5, 'Ism5', 'Familiya5', 'email5@example.com', '888888888', '2023-11-01', 'JOB5', 90000, 0.5, 6, 10),
    (6, 'Ism6', 'Familiya6', 'email6@example.com', '777777777', '2023-11-02', 'JOB6', 100000, 0.6, 7, 50),
    (7, 'Ism7', 'Familiya7', 'email7@example.com', '666666666', '2023-11-03', 'JOB7', 110000, 0.7, 8, 40),
    (8, 'Ism8', 'Familiya8', 'email8@example.com', '555555555', '2023-11-04', 'JOB8', 120000, 0.8, 9, 50),
    (9, 'Ism9', 'Familiya9', 'email9@example.com', '444444444', '2023-11-05', 'JOB9', 130000, 0.9, 10, 40),
    (10, 'Ism10', 'Familiya10', 'email10@example.com', '333333333', '2023-11-06', 'JOB10', 140000, 1.0, 11, 40);
    """
    
sql1 = "SELECT FIRST_NAME, LAST_NAME, SALARY, DEPARTMENT_ID FROM employee WHERE DEPARTMENT_ID = 40;"

mycursor = mydb.cursor()
mycursor.execute(sql)
mycursor.execute(sql1)
result1 = mycursor.fetchone()
print(result1)
