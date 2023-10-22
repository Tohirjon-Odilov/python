import mysql.connector

# MySQL serverga bog'lanish
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="city"
)

# SQL so'rovni yaratish
sql = "SELECT COUNT(*) FROM city WHERE population > 1000000"
sql2 = "SELECT COUNT(*) FROM city WHERE population < 1000000"

# Cursor yaratish
mycursor = mydb.cursor()

# SQL so'rovlarni bajarish
mycursor.execute(sql)
result1 = mycursor.fetchone()[0]

mycursor.execute(sql2)
result2 = mycursor.fetchone()[0]

# Natijalarni chiqarish
print(f"Aholi soni 1 milliondan ko'p bo'lgan shaharlar soni: {result1}")
print(f"Aholi soni 1 milliondan kam bo'lgan shaharlar soni: {result2}")
