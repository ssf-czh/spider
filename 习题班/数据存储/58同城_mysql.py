'''
爬取58同城中的某一件商品
这里以笔记本为例
利用自制的mysqlAPI 储存到mysql

'''
import requests
from lxml import etree
from 习题班.数据存储.ApiDemo import Mysql_demo

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }

def f_e_spider():

    url = 'https://fz.58.com/bijibendiannao/?key=%E7%AC%94%E8%AE%B0%E6%9C%AC%E8%BD%AC%E8%AE%A9&cmcskey=%E7%AC%94%E8%AE%B0%E6%9C%AC%E8%BD%AC%E8%AE%A9&jump=3&searchtype=1&sourcetype=5&upcatelistname=bijibendiannao#'
    # url = 'https://fz.58.com/bijibendiannao/?key=%E7%AC%94%E8%AE%B0%E6%9C%AC%E8%BD%AC%E8%AE%A9&cmcskey=%E7%AC%94%E8%AE%B0%E6%9C%AC%E8%BD%AC%E8%AE%A9&jump=3&searchtype=1&sourcetype=5&upcatelistname=bijibendiannao'
    rsp = requests.get(url, headers=headers)
    # print(rsp.text)
    return rsp.text

def get_detail(url):

    # print(url)
    rsp =requests.get(url, headers=headers)
    html = rsp.text
    html = etree.HTML(html)
    # print(html)
    try:
        title = html.xpath("//div[@class='detail-title']//h1[@class='detail-title__name']/text()")[0].strip('\r').strip()
    except:
        title = None
    # print(title)
    try:
        time = html.xpath("//div[@class='detail-title__info__text']/text()")[0].split(" ")[0]
        # print(time)
    except:
        time =None
    try:
        price = html.xpath("//span[@class='infocard__container__item__main__text--price']/text()")[0].strip("\r\n\t\t\t\t\t\t\t\t    \t\t\t\t\t\t    \t\t\t\t\t\t\t    \t\t\t\t\t\t")
        # print(price)
    except:
        price = None
    try:
        addr = html.xpath("//div[@class='infocard__container__item__main']//a//text()")
        if len(addr) > 1:
            addr = addr[0] + "-" + addr[1]
        else:
            addr = addr[0]
            # print(addr)
    except:
        addr = None
    try:
        details = html.xpath("//article[@class='description_con']//text()")
        # print(details)
        detail = ''
        for i in details:
            detail = detail + i
    except:
        detail = None
    return {
        "title": title,
        "time": time,
        "price": price,
        "addr": addr,
        "detail": detail
    }


def to_mysql(data):
    print(data)
    mysql = Mysql_demo.Mysql_API("localhost", "root", "12345", "58同城")
    mysql.insert_mysql("laptop", data=data)



def down_load(html):
    html = etree.HTML(html)
    urls = html.xpath("//td[@class='t']/a[@class='t']/@href")
    for url in urls:
        if "https:" not in url:
            url = "https:" + url
        data = get_detail(url)
        to_mysql(data)


if __name__ == '__main__':
    html = f_e_spider()
    down_load(html)