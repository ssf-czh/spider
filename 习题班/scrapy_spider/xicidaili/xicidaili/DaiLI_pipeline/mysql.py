
from scrapy_spider.xicidaili.xicidaili import settings
import pymysql

db = pymysql.connect(host= settings.host, user= settings.user, password= settings.password, port= 3306, database= settings.database)
cursor = db.cursor()
class Sql():
    @classmethod
    def insert_to_sql(clas, item):
        item = dict(item)
        table = "dailis"
        keys = ",".join(item.keys())
        values = ",".join(["%s"] * len(item))
        sql = "INSERT INTO {}({}) values ({})".format(table, keys, values)
        print(sql)
        try:
            cursor.execute(sql, tuple(item.values()))
            db.commit()
            print("成功")
        except Exception as e:

            print(e, "失败")



