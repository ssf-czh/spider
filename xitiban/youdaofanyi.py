'''
抓取有道翻译

POST：
i: cat
salt: 15491734636247   //salt 时间戳
      1549173730.815766 * 10000
sign: c0c8f311e37faf54391f6bcd244bcea6 //通过js来的
ts: 1549173463624

解析：
salt 通过寻找每个的js文件查找salt关键词
发现salt = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10)  对应python中就是 time.time()+int(random(10))
同理 sign = n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")  这里的e是需要翻译的单词



i: job
salt: 15491734113560
sign: 3f4c723cbd1cb55c56d35b9a8c33f46f
ts: 1549173411356

'''
from urllib import  request,parse
import time
import random
import hashlib
import json
# hashlin是md5

# 解析：
# salt 通过寻找每个的js文件查找salt关键词
# 发现salt = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10)  对应python中就是 time.time()*1000+int(random(10))
# 同理 sign = n.md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")  这里的e是需要翻译的单词
def getMd5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding="utf-8"))
    sign = md5.hexdigest()

    return sign
def Parse(content):
    '''
    解析json格式
    :param content:
    :return:
    '''
    data_json = json.loads(content)
    for item in data_json["smartResult"]["entries"]:
        print(item)
def yd_fanyi(key):
    base_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    ts= int(time.time() * 1000)
    salt = ts * 10 + + random.randint(0,10)
    sign ="fanyideskweb" + key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": getMd5(sign),
        "ts": ts,
        "bv": "9c4fffad2fb69d08cd130e408e0f8108",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }
    data= parse.urlencode(data)

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-109631377@10.168.8.76; OUTFOX_SEARCH_USER_ID_NCOO=1695312360.5301702; JSESSIONID=aaaJsY2t4jz_XfEyq7XIw; ___rl__test__cookies=1549174401270",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url= base_url, data= bytes(data, encoding="utf-8"), headers= headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    Parse(html)
    # print(rsp.read().decode())



if __name__ == '__main__':
    key = input("请输入需要翻译的单词：")
    yd_fanyi(key)
