# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from 习题班.scrapy_spider.Meiju_spider.Meiju_spider.items import MeijuSpiderItem
class MeijuSpider(scrapy.Spider):
    name = 'Meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        # print(response.body.decode())
        # response.selector.xpath("//ul[@class='top-list  fn-clear']//li")
        html = etree.HTML(response.body.decode("GBK"))
        movies = html.xpath("//ul[@class='top-list  fn-clear']//li")
        for movie in movies:
            # print(movie)
            movie_name = movie.xpath("./h5/a")[0].text #电影名
            # print(movie_name)
            status = movie.xpath("./span[@class='state1 new100state1']/font")[0].text #状态
            # print(status)

            item = MeijuSpiderItem()

            item["name"] = movie_name
            item["status"] = status
            yield item
