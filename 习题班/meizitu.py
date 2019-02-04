'''
爬取妹子图
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

    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "]
    headers = {
        "User-Agent": random.choice(my_headers),
        'Upgrade - Insecure - Requests': "1"
    }
    rsp = requests.get(url ="https://i.meizitu.net/2014/03/20140307jp01.jpg",headers=headers)
    print(rsp.status_code)
    with open("666", "wb") as f:
        f.write(rsp.content)
