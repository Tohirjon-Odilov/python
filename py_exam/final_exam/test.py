import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="city"    
)

sql = "select count(*) from city where population > 1000000"
sql1 = "select count(*) from city where population < 1000000"

mycursor = mydb.cursor()
mycursor.execute(sql)
print(mycursor.fetchone())