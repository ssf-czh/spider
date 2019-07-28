'''
爬取妹子图
xpath
'''
import requests,os
from lxml import etree
import random
def mz_spider(url):
    # print(22)
    headers ={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    rsp = requests.get(url= url,headers= headers)
    print(rsp.status_code)
    # print(rsp.text)
    html = etree.HTML(rsp.text)
    urls = html.xpath("//div[@class='postlist']/ul/li/span/a/@href")
    # print(urls)
    for url in urls:
        print(url)

        image_parse(url)


def image_parse(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    rsp = requests.get(url=url, headers=headers)
    print(rsp.status_code)
    html = etree.HTML(rsp.text)
    title =html.xpath("//h2/text()")[0]
    pages = html.xpath("//div[@class='pagenavi']/a/span/text()")[-2]
    print(pages,type(int(pages)))
    for page in range(1,int(pages)):
        # print(page)
        image_url = url + "/" + str(page)
        # print(image_url)
        image_down(image_url, title)

def image_down(image_url,title):
    # print(22)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    rsp = requests.get(url=image_url, headers=headers)
    html = etree.HTML(rsp.text)
    image_src = html.xpath("//p/a/img/@src")[0]

    image_rsp = requests.get(url= image_src,headers =headers)
    print(image_rsp.status_code ,"!")

    root_dir = "mz_img"
    image_name = image_src.split("/")[-1]
    title = title.replace(" ","")
    root_dir = root_dir+"\\"+title
    print(root_dir)
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    with open(root_dir+"\\"+image_name, "wb")as f:
        f.write(image_rsp.content)
        print("完成"+title+"....")






if __name__ == "__main__":

    # for page in range(1,2):
    #     base_url = "https://www.mzitu.com/mm/page/{}/".format(str(page))
    #     mz_spider(base_url)


    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Host": "i.meizitu.net",
        'Upgrade - Insecure - Requests': "1",

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64;rv:64.0) Gecko/20100101 Firefox/64.0"
        # "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        # 'Upgrade - Insecure - Requests': "1"
    }
    proxies = {
        "http": "110.52.235.85:9999"
    }
    rsp = requests.get(url = "https://i.meizitu.net/2019/01/06a05.jpg", headers =headers)
    print(rsp.status_code)
    # print(rsp.text)
    with open("666.jpg", "wb") as f:
        f.write(rsp.content)
