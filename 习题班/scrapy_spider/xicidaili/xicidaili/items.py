# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XicidailiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiciDailiItem(scrapy.Item):
    country = scrapy.Field()
    ipaddress = scrapy.Field()
    port = scrapy.Field()
    severaddr = scrapy.Field()
    isniming = scrapy.Field()
    type = scrapy.Field()
    alivetime = scrapy.Field()
    testtime  = scrapy.Field()