import pymysql
db = pymysql.connect(host="127.0.0.1", user="root", password="12345", db="xicidaili",port=3306)
print(db)
db.close()