'''
今日头条爬取
ajax图片
'''
import requests
import json as js
import random
from urllib.parse import urlencode
url = "https://www.toutiao.com/search_content/"
def one_page(page):
    params = {

        "offset": page,
        "format": "json",
        "keyword": "美女街拍",
        # "keyword": "%E7%BE%8E%E5%A5%B3%E8%A1%97%E6%8B%8D",
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
        "from": "search_tab",
        "pd": "synthesis"
    }
    # print(url+"?"+urlencode(params))
    # rsp = requests.get(url = url+"?"+urlencode(params))
    rsp = requests.get(url =url,params = params)
    return rsp.json()
def parse_page(json):
    # with open("ttt.txt","w") as f:
        # f.write(js.dumps(json))
    print(json["data"])
    items = json.get("data")
    for item in items:
        image_urls = item.get("image_list")
        if type(image_urls) is list:
            for image_url in image_urls:
                print(image_url)
                # if image_url["url"] == "//p3-tt.bytecdn.cn/list/dfic-imagehandler/dbdaa0c6-2d3e-45d5-b7c1-78641ddaf212":
                #     print("YES")
                yield image_url.get("url")
def save_image(image_url):
    rsp = requests.get("http:" + image_url)
    path ="./images/" + str(random.randint(0,100000)) +'.jpg'
    print(path)
    # cnt += 1
    with open(path, "ab") as f:
        f.write(rsp.content)
if __name__ == '__main__':
    for page in range(3):
        json = one_page(page*20)
        for image_url in parse_page(json):
            pass
            # print(image_url)
            # rsp = requests.get("http:" + image_url)
            # with open("texxt.jpg","ab") as f:
            #     f.write(rsp.content)

    #         print(rsp.content)
            save_image(image_url)
    #         with open("./images/ttt.txt","w")as f:
                # f.write("123")


    # with open("texxt.jpg","ab") as f:
        # f.write(requests.get("http://p3-tt.bytecdn.cn/list/pgc-image/15367210717753c286df9df").content)
