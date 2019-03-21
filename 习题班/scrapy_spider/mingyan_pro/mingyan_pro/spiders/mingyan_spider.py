# -*- coding: utf-8 -*-
import scrapy
from mingyan_pro.items import MingyanProItem


class MingyanSpiderSpider(scrapy.Spider):
    name = 'mingyan_spider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):

        print("当前在爬取{}".format(response.url))
        print("*"*20)
        item = MingyanProItem()
        divs = response.xpath("//div[@class='quote post']")
        print(len(divs))
        for div in divs:
            text = div.xpath("./span[@class='text']/text()").extract()[0]
            author = div.xpath(".//small[@class='author']/text()").extract()[0]
            tag = div.xpath(".//a[@class='tag']/text()").extract()
            item["text"] = text
            item["author"] = author
            item["tag"] = tag

            yield item

        print("*" * 20)
        urls = ["http://lab.scrapyd.cn/page/{}/".format(str(i)) for i in range(2,7)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

