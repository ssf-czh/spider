'''
非关系型数据库
MongoDB
由 多个数据库构成
一个数据库由多个集合构成//相当于关系型中的表
一个集合由多个文档构成//相当于关系型中的行
文档是由多个字典构成的

可以插入相同的文档 但是每插入一次 _id值是不同的
'''

import pymongo
# 建立一个客户端对象
client = pymongo.MongoClient(host ="localhost", port= 27017)
# 指定一个数据库
db = client.test
# db = client["test"]

# 指定一个集合
collection = db.student
# collection = db["student"]

# 往一个集合中插入数据
student1 = {
    # _id如果没有指定 插入的时候系统会自动加上唯一的_id
    # _id: 1236516516
    "id": "20170101",
    "name": "Jordan",
    "age": 20,
    "gender": "male"
}
# res = collection.insert_one(student1)
# print(type(res),res.inserted_id)

# 如果插入多条
student2 = {
    # _id如果没有指定 插入的时候系统会自动加上唯一的_id
    # _id: 1236516516
    "id": "20170202",
    "name": "Mike",
    "age": 21,
    "gender": "male"
}
resb = collection.insert_many([student1, student2,{
    "name": "qqq",
    "age": 20
}])
print(resb.inserted_ids)
# print(resb.inserted_id)

# 查找集合中的文档
# find_one 是查找单个结果
result = collection.find_one({"name": "Mike"})
print(result)
from bson.objectid import ObjectId
# print(collection.find_one({"_id": ObjectId("5c2dd32d0adc701e78e2f53b")})
# find()返回符合条件的结果 类型是Cursor 相当于生成器 可迭代
# results = collection.find({"age": 20})
# i = 1
# for res in results:
#     print(i, res)
#     i += 1

# .count()方法返回目标数量
results = collection.find({"age": 20})
for i in results:
    print(i)
print(collection.find().count())
print(collection.find({"age": 21}).count())

# find().sort()按照指定方法排序 需要查询
# .find().skip(k) 偏移k个 就是忽略前k个 需要自己查询

# 更新 对于查询后的数据 如要要增加一点东西
condition = {"name": "Kevin"}
collection.insert_one(condition)
student = collection.find_one(condition)
student["age"] = 25
ress = collection.update(condition, student)
print(ress)

anss = collection.find()
for ans in anss:
    print(ans)

# 删除文档
res = collection.delete_one({"name": "Jordan"})
print(res,res.deleted_count)
res = collection.delete_many({"age": {"$lt": 25}})
print(res,res.deleted_count)