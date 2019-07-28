# -*- coding: utf-8 -*-
import scrapy


class BaiduSpiderSpider(scrapy.Spider):
    #爬虫名称 scrapy genspider
    name = 'Baidu_spider'
    #允许爬取的域名
    allowed_domains = ['baidu.com']
    #爬虫的起始地址
    start_urls = ['http://baidu.com/']

    #重写parse方法
    def parse(self, response):
        with open("baidu.html", "w", encoding="utf-8") as f:
            f.write(response.body.decode())
