# -*- coding: utf-8 -*-
import scrapy
from xicidaili.items import XiciDailiItem

class XicidailiSpider(scrapy.Spider):
    name = 'Xicidaili'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        # print(response.text)
        daili_1 = response.xpath("//tr[@class='odd']")
        daili_2 = response.xpath("//tr[@class='']")
        dailis = daili_1 + daili_2
        count = 0
        for daili in dailis:
            item = XiciDailiItem()
            item["ipaddress"] = daili.xpath("./td[2]/text()").extract()[0]
            item["country"] = "chiana"
            item["port"] = daili.xpath("./td[3]/text()").extract()[0]
            item["severaddr"] = daili.xpath("./td[4]/text()").extract()[0]
            item["isniming"] = daili.xpath("./td[5]/text()").extract()[0]
            item["type"] = daili.xpath("./td[6]/text()").extract()[0]
            item["alivetime"] = daili.xpath("./td[7]/text()").extract()[0]
            item["testtime"] = daili.xpath("./td[8]/text()").extract()[0]
            count = count + 1
            print(count)
            print(item)
            yield item
            


