# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy_spider.lianjia.lianjia import settings
import pymongo

# db = pymongo.MongoClient("localhost", 27017)
# db = db.lianjia
# collection = db["cols"]
# print(collection)

class LianjiaPipeline(object):
    def process_item(self, item, spider):
        return item

class To_mongo(object):
    def __init__(self):
        # print("我初始化了！！！！！")
        self.client = pymongo.MongoClient(host= settings.MONGO_HOST, port= settings.MONGO_PORT)
        self.db = self.client["lianjia"]
        self.collection = self.db[settings.COLLECTION]
        # print(self.collection,"************")
    def process_item(self, item, spider):

        try:
            self.collection.insert_one(dict(item))
            print("插入成功")
            return item
        except Exception as e:
            print("插入失败--", e)