# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    time = scrapy.Field()
    house_id = scrapy.Field()
    base_info = scrapy.Field()
    house_direction = scrapy.Field()
    house_scale = scrapy.Field()
    house_daxiao = scrapy.Field()


