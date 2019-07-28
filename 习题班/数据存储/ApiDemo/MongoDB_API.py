from pymongo import MongoClient

class MongoDB():
    def __init__(self, host, port, db, table):
        self.host = host
        self.port = port
        self.client = MongoClient(host=self.host, port=self.port)
        self.db = self.client[db]
        self.table = self.db[table]

    # 获取一条数据
    def get_one(self, query):
        return self.table.find_one(query, property={"_id":False})

    # 获取多条数据
    def get_all(self, query):
        return self.table.find(query)

    # 添加数据
    def add(self, kv_dict):
        return self.table.insert_one(kv_dict)

    # 删除数据
    def delete(self, query):
        return self.table.delete_many(query)

    # 查看集合中是否包含满足的数据 如果有返回True
    def check(self, query):
        return self.table.find_one(query)
