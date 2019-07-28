'''
百度壁纸是ajax
爬取百度壁纸
'''
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
}
url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8+%E4%B8%8D%E5%90%8C%E9%A3%8E%E6%A0%BC+%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%A3%81%E7%BA%B8+%E4%B8%8D%E5%90%8C%E9%A3%8E%E6%A0%BC+%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&itg=1&gsm=1e&1549467788960="
rsp = requests.get(url, headers=headers)
rsp.encoding = rsp.apparent_encoding
print(rsp.text)