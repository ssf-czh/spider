# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import  pymongo

db = pymongo.MongoClient("localhost", 27017)
db = db.xicidaili
collection = db.dailis

class XicidailiPipeline(object):
    def process_item(self, item, spider):
        dic = dict(item)
        collection.insert_one(dic)
        return item
