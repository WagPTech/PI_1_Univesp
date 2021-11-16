import pymysql

db = pymysql.connect("localhost", "univesp", "Univesp123@", "univesp")

cursor = db.cursor()
sql = "SELECT * FROM ativos"
cursor.execute(sql)
results = cursor.fetchall()
