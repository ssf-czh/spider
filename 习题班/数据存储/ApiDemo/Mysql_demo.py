'''
Mysql 数据库的简单demp
1:增加 插入
2：删除
3：修改 更新
4：查询
5：.......
'''

__author__ = 'ssf-czh'

import pymysql

class Mysql_API():
    def __init__(self, host, user, passwd, dbname):
        self.db = pymysql.connect(host=host, user=user, password=passwd, db=dbname,port=3306)
        self.cursor = self.db.cursor()


    #插入数据
    def insert_mysql(self,tablename,data):
        keys = ','.join(data.keys())
        values = ','.join(["%s"] * len(data))
        sql = '''
        insert into {tablename}({keys}) values({values})
        '''.format(tablename=tablename, keys=keys, values=values)
        # print(sql)
        try:
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
            return self.cursor.lastrowid
            print("successful")
        except Exception as e:
            print(e)
            self.db.rollback()
            return None


    #删除数据
    def delete_mysql(self, tablename, condition):
        #query:age>10
        sql = 'delete from {tablename} where({condition}) '.format(tablename=tablename, condition=condition)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(e)
            self.db.rollback()
            return None

    #更新数据
    def update_mysql(self, tablename, update_mess, condition):
        sql = 'update {tablename} set {update_mess} where {condition}'.format(tablename=tablename, update_mess=update_mess, condition=condition)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.db.rollback()

    #查询数据

    # 查询一条数据
    def find__one_mysql(self, tablename, condition):
        sql = "select * from {tablename} where {condition}".format(tablename=tablename, condition=condition)
        print(sql)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            self.db.rollback()
    # 查询所有数据
    def find_all_mysql(self,tablename, condition):
        sql = "select * from {tablename} where {condition}".format(tablename=tablename, condition=condition)
        print(sql)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            self.db.rollback()


    def clean_mysql(self,tablename):
        sql = 'truncate table {tabname}'.format(tabname=tablename)
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)


db = Mysql_API("127.0.0.1", "root", "12345", "xicidaili")
# db = pymysql.connect(host="127.0.0.1", user="root", password="12345", db="xicidaili",port=3306)
print(db)
db.close()