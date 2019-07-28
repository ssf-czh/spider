# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MeijuSpiderPipeline(object):
    def __init__(self):
        self.f = open("meiju.json", 'w', encoding="GBK")
    def process_item(self, item, spider):
        json.dump(dict(item), open("meiju.json", "a"), ensure_ascii=False)
        return item
    def close_spider(self):
        self.f.close()
