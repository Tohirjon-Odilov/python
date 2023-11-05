import mysql.connector


db = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     password = 'root'
)

if db.is_connected():
     print('Ulandi.')
