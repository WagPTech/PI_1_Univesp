# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="univesp",
  password="Univesp123@",
  database="univesp"
)

cursor = connection.cursor()

#sql = "SELECT * FROM ativos"
#sql = "SELECT CODNEG FROM ativos WHERE CODNEG = \'VALE3\';"
sql = "SELECT table_schema \"Univesp\", ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) \"Size(MB)\" FROM information_schema.tables GROUP BY table_schema;"

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
  print(result)
