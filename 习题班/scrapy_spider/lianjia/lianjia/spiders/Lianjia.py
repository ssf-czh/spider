# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_spider.lianjia.lianjia import settings
from scrapy_spider.lianjia.lianjia.items import LianjiaItem
headers = settings.DEFAULT_REQUEST_HEADERS

class LianjiaSpider(scrapy.Spider):
    name = 'Lianjia'
    # allowed_domains = ['www.lianjia.com']
    # start_urls = ['http://www.lianjia.com/']
    def start_requests(self):
        start_urls = ["https://fz.lianjia.com/zufang/jinanqu1/pg1/#contentList",
                      "https://fz.lianjia.com/zufang/gulou3/pg1/#contentList"]
        for url in start_urls:
            yield Request(url, headers= headers, callback=self.parse)
    def parse(self, response):
        # print(type(response.url),response.url,"************************")
        # print(response.text)
        hrefs = response.xpath("//div[@class='content__list--item--main']//p[@class='content__list--item--title twoline']/a/@href").extract()
        # print(len(hrefs))
        for href in hrefs:
            href = "https://fz.lianjia.com" + href
            yield Request(href, headers=headers, callback=self.detail_parse)
        current_page = response.url.split("/")[-2]
        current_page = int(current_page.strip("pg"))
        current_page_str = str(current_page)

        if current_page < 6 :
            next_url = response.url.rstrip(current_page_str + "/")+ str(current_page + 1) + "/"
            # print(next_url)
            yield Request(next_url, callback=self.parse, headers= headers)

    def detail_parse(self,response):

        item = LianjiaItem()
        try:
            title = response.xpath("//p[@class='content__title']/text()").extract()[0]
            print(title)
            price = title.split()[-1]
        except Exception as e:
            print(response.url)
            print("失败**************************************************")

        try:
            time = response.xpath("//div[@class='content__subtitle']/text()").extract()[1].split()[-1]
            # print(time,"!!!!!!!!!!!!!!!!!!!!!!!!")

        except Exception as e:
            print(response.url)
            print("失败**************************************************")

        try:

            house_id = response.xpath("//div[@class='content__subtitle']/i[@class='house_code']/text()").extract()[0].split("：")[-1]
            # print(house_id,"!!!!!!!!!!!!!!!!!!!!!!!!")

        except Exception as e:
            print(response.url)
            print(e,"失败**************************************************")

        try:

            base_info = ",".join(response.xpath("//div[@class='content__article__info']//li/text()").extract())
            # print(base_info,"!!!!!!!!!!!!!!!!!!!!!!!!")

        except Exception as e:
            print(response.url)
            # print(e,"失败**************************************************")

        try:

            house_direction = response.xpath("//p[@class='content__article__table']/span[4]/text()").extract()[0]
            house_scale = response.xpath("//p[@class='content__article__table']/span[2]/text()").extract()[0]
            house_daxiao = response.xpath("//p[@class='content__article__table']/span[3]/text()").extract()[0]
            # print(house_direction,"!!!!!!!!!!!!!!!!!!!!!!!!")

        except Exception as e:
            print(response.url)
            print(e,"失败**************************************************")


        item["title"] = title
        item["price"] = price
        item["time"] = time
        item["house_id"] = house_id
        item["base_info"] = base_info
        item["house_direction"] = house_direction
        item["house_scale"] = house_scale
        item["house_daxiao"] = house_daxiao
        yield item
