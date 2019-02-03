'''
代理的使用
'''
# urllib使用代理
import urllib
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy = "119.101.117.39:9999"
#
# proxy_hander = ProxyHandler({
#     "http": "http://" + proxy,
#     "https": "https://" + proxy
# })
# opener = build_opener(proxy_hander)
# # opener = build_opener()
# try:
#     print(6789)
#     rsp = opener.open("http://httpbin.org/get")
#     print(rsp.read().decode())
# except URLError as e:
#     print(e.reason)

# 利用request使用代理服务
import requests
proxy = "119.101.114.125:9999"

proxies = {
    "http": "http://" + proxy,
    "https": "https://" + proxy
}

try:
    rsp = requests.get("http://httpbin.org/get", proxies= proxies)
    print(type(rsp.text))
    print(rsp.text)
except Exception as e:
    print("wrong")
    print(e)


# 利用selenium进行代理服务
from selenium import webdriver

proxy = "119.101.114.125:9999"
chrom_options = webdriver.ChromeOptions()
chrom_options.add_argument("--proxy-server=http://" + proxy)
browser = webdriver.Chrome(chrome_options=chrom_options)
# browser = webdriver.Chrome()
browser.get("http:httpbin.org/get")