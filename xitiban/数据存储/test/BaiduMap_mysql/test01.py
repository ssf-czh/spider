'''
爬取百度地图里的信息
百度地图给web服务提供了API
http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
'''
import requests

def BaiduMap_spider(page_num):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    url = "http://api.map.baidu.com/place/v2/search"
    params = {
        "query": "公园",
        "region": "福州市",
        "scope": 2,
        "output": "json",
        "page_size": 20,
        "page_num": page_num,
        "ak": "KFHfhl5y3Z2ByaxsFHScb4fPHcIQ6i39",
    }
    rsp = requests.get(url, headers=headers, params=params)
    print(rsp.json())
    data = rsp.json()
    for park in data["results"]:
        park_name = park["name"]
        park_add =  park["address"]
        mess = park_name + "\t" + park_add + '\n'
        # with open("parks.txt", "a", encoding="utf-8") as f:
        #     f.write(mess)
if __name__ == '__main__':
    for page_num in range(10):
        BaiduMap_spider(page_num)