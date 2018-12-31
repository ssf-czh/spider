import  requests
import json
from bs4 import BeautifulSoup
from urllib import request

url = "http://www.baidu.com"
# rsp = request.urlopen(url)
rsp  = requests.get(url)
rsp.encoding="utf-8"

html = rsp.text

# html = rsp.read()
# print(type(html))
soup = BeautifulSoup(html, "lxml")
html = soup.prettify()

# print(type(html))
print(html)
# print("=="*20)
# print(soup.head)
# print("=="*20)
# print(soup.meta)
# print("=="*20)
print(type(soup.link))
print(soup.link.attrs)

