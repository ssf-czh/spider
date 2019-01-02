# import pymysql
# db = pymysql.connect(host= "localhost",user= "root",password= "12345", port= 9686)
# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print(data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()

from selenium import webdriver
browser = webdriver.Chrome()