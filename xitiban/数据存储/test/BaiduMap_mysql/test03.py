'''
将test02获得的park数据 （uid）拿出来
并且利用百度地图api     http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求
地点详情服务 进行详细咨询
uid
output


'''
import requests
from 习题班.数据存储.test.BaiduMap_mysql.MysqlAPI import SQL

def get_json(uid):
    # print(666)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    params = {
        "uid": uid,
        "output": "json",
        "scope": 2,
        "ak": "KFHfhl5y3Z2ByaxsFHScb4fPHcIQ6i39",

    }
    rsp = requests.get(url="http://api.map.baidu.com/place/v2/detail", headers=headers, params=params)
    # print(rsp.text)
    return rsp.json()
def detail_spider(datas):
    # datas = ('a9173a180c1324641df74dd3',), ('9044abbcd372cdb6e115f9f2',), ('c8e8f63374c13411ab0dd831',), ('db1f39d4badf396ef5c59c47',)

    for data in datas:
        data_json = get_json(data[0])
        # print(data_json)
        status = data_json["status"]
        if status == 0:
            try:
                uid = data_json["result"]["uid"]
            except:
                uid = None
            try:
                name = data_json['result']["name"]
            except:
                name = None
            try:
                address = data_json['result']["address"]
            except:
                address = None
            try:
                content_tag = data_json['result']["detail_info"]['content_tag']
            except:
                content_tag = None
                # print(uid, name, address, content_tag)
            SQL.park_info_insert(uid, name, address, content_tag)


if __name__ == '__main__':
    data = SQL.find_mess()
    detail_spider(data)