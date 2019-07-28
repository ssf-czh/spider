'''
将test01 得到的数据传入mysql

{
    "name": "福州西湖公园",
    "location": {
        "lat": 26.099417,
        "lng": 119.296415
    },
    "address": "福州市鼓楼区湖滨路70号",
    "province": "福建省",
    "city": "福州市",
    "area": "鼓楼区",
    "street_id": "fe9271184079c889adcb6660",
    "telephone": "(0591)83783655,(0591)83783767",
    "detail": 1,
    "uid": "fe9271184079c889adcb6660",
    "detail_info": {
        "tag": "旅游景点;公园",
        "navi_location": {
            "lng": 119.29686558716,
            "lat": 26.096622950798
        },
        "type": "scope",
        "detail_url": "http://api.map.baidu.com/place/detail?uid=fe9271184079c889adcb6660&output=html&source=placeapi_v2",
        "overall_rating": "4.2",
        "comment_num": "366",
        "children": [ ]
    }
}
'''
import requests
from 习题班.数据存储.test.BaiduMap_mysql.MysqlAPI import  SQL
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
    # print(rsp.json())
    data = rsp.json()
    print(data)

    for park in data["results"]:
        print(park)
        SQL.mysql_insert(park["name"], park["address"], park["uid"])


if __name__ == '__main__':
    for page_num in range(10):
        BaiduMap_spider(page_num)