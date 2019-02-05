'''
数据存储之mysql

'''

import pymysql



# try:
#     # 获取一个数据库连接
#     # 打开数据库连接
#     '''
#     db = pymysql.connect(host="localhost", user="root", passwd="12345",db="ceshi", port=3306)
#     host:请求数据库ip地址 localhost默认本机ip
#     user:登入数据库的用户
#     passwd:登入用户的密码
#     db:数据库名称
#     port：端口号 mysql默认端口号是3306
#     '''
#
#     # 创建数据库中的表（头）
#
#
#     db = pymysql.connect(host="localhost", user="root", passwd="12345",db="ceshi", port=3306)
#     print(db)
#     # 是通过游标实现的
#     cursor = db.cursor()
#     # sql语句都是用过cursor.execute()来执行的
#     # cursor.execute("f exists TEST drop table i")#如果创业板在test表就删除它
#     # 预处理语句
#     # 创建表示有格式要求的
#     sql = '''CREATE TABLE test(
#     FIRST_NAME CHAR(20),
#     AGE INT
#     )
#     '''
#     try:
#         cursor.execute(sql)
#     except:
#         print("fail")
#     cursor.close()
# except:
#     pass


# 往表里面插入内容

# db = pymysql.connect(host="localhost", user="root", passwd="12345",db="ceshi", port=3306)
# cursor = db.cursor()
# # sql = '''
# # INSERT INTO test(FIRST_NAME,AGE)VALUES("ssf",20)
# #
# # '''
#
# sql = '''
#     INSERT INTO test(FIRST_NAME,AGE)VALUES("%s",%d)
# '''%("ssf-czh", 20)
#
# try:
#     cursor.execute(sql)
#     # 注意 此处还需要db.commit下 因为具有事务性
#     db.commit()
#     print("yes")
# except Exception as e:
#     print("no")



# 查询表中的信息
db = pymysql.connect(host="localhost", user="root", passwd="12345",db="ceshi", port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM test")#查找test表中的所有内容
print(cursor.rowcount)#返回受影响的条数
# datas = cursor.fetchall()#通过fetchall函数取出所有内容 是一个元祖
data = cursor.fetchone()#游标下的第一条 没查一次游标下移一次

# print(datas)
print(data)
print(cursor.fetchone())

