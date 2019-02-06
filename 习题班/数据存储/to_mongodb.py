'''
mongodb：非关系型数据库（NOSQL 不仅是关系型数据库）
mongodb 更适合于爬虫
是一个基于分布式文件存储的数据库，c++编写，速度快
主要为web应用提供可扩展的高性能数据存储解决方案
概念说明:
SQL:            MongoDB:        说明：
database        database        数据库
table           collection      表/集合
row             document        行/文档
column          field           字段/域
index           index           索引
primary         primary         主键/_id为主键
'''

import pymongo


# 查询数据

# 连接客户端
# client = pymongo.MongoClient(host="localhost", port=27017)
# # 获得数据库
# db = client.test
# # print(db)
# # 获取集合
# col = db.student
# # 获取数据
# datas = col.find()
# print(datas)
# for data in datas:
#     print(data["_id"])


# 插入数据


# client = pymongo.MongoClient(host="localhost", port=27017)
# db = client.ssf  #如果没有这个数据库 就默认创建一个数据库 类似于字典
# print(db)
# info = {
#     "name": "czh",
#     "age": "20",
#     "course": ["spider", "database", "python_web"]
# }
#
# posts = db.posts #创建一个集合对象
# res = posts.insert_one(info)
# print(res, res.inserted_id)

# client = pymongo.MongoClient(host="localhost", port=27017)
# # 获得数据库
# db = client.ssf
# # print(db)
# # 获取集合
# col = db.posts
# # 获取数据
# datas = col.find()
# print(datas)
# for data in datas:
#     print(data["course"])