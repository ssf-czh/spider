'''
Ajax 异步加载
通过调试工具 查看XHR 发现加载出来的url
https://www.pexels.com/?dark=true&page=2&format=js&seed=2019-02-06%2008:15:31%20+0000
https://www.pexels.com/?dark=false&format=js&page=3&seed=2019-02-06+08%3A15%3A31++0000&format=js&seed=2019-02-06%2008:15:31%20+0000
https://www.pexels.com/?dark=true&format=js&page=4&seed=2019-02-06+08%3A15%3A31++0000&format=js&seed=2019-02-06%2008:15:31%20+0000
https://www.pexels.com/?dark=false&format=js&page=5&seed=2019-02-06+08%3A15%3A31++0000&format=js&seed=2019-02-06%2008:15:31%20+0000

发现许多参数都一样的 去掉
https://www.pexels.com/?page=2 3 4 5
'''
from bs4 import BeautifulSoup
from lxml import etree
import requests
import os
import time

def spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    rsp = requests.get(url=url, headers=headers)
    # print(rsp.text)
    html = etree.HTML(rsp.text)
    img_urls = html.xpath("//article[@class='photo-item photo-item--overlay']//img[@class='photo-item__img']/@src")#可以直接获取所有标签下的属性 并且组成列表
    print(img_urls,type(img_urls))
    # soup = BeautifulSoup(rsp.text, "lxml")
    # img_urls = soup.select("article[class='photo-item photo-item--overlay'] a[class='js-photo-link photo-item__link'] img[class='photo-item__img']")#不可以直接获得属性 必须要获得标签后遍历标签得到属性
    # # print(img_urls)
    # for img_url in img_urls:
    #     u = img_url["src"]
    #     print(u, type(img_url))

    # print(img_urls)
    for img_url in img_urls:
        download_img(img_url)
def download_img(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    rsp = requests.get(url=url, headers=headers)
    dir = "ajax_imag"
    if not os.path.exists(dir):
        os.mkdir(dir)
    jpg_name = url.split("?")[0].split("/")[-1]
    with open(dir + "\\" + jpg_name, "wb") as f:
        print("...")
        f.write(rsp.content)

if __name__ == "__main__":
    urls = ["https://www.pexels.com/?page={}".format(str(i)) for i in range(1, 2)]
    for url in urls:
        # print(1)
        time.sleep(1)
        spider(url)



'''



























pn: 30

1549467788960: 
https://image.baidu.com/search/acjson?pn=30&1549467788960=


'''