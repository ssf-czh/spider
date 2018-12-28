'''
构建代理队列
每次访问服务器， 随机抽取一个代理
抽取可以用 random.choice

1：构建代理队列
2: 每次访问，随机抽取代理并执行
'''
from urllib import request,error

proxy_list=[
    {"http":"113.105.248.35:80"},
    {"http":"111.13.16.40:80"},
    {"http":"220.170.49.107:80"},
    {"http":"61.19.145.66:8080"}
]

proxy_hander_list = []
for proxy in proxy_list:
    proxy_hander = request.ProxyHandler(proxy)
    proxy_hander_list.append(proxy_hander)

opener_list = []
for proxy_hander in proxy_hander_list:
    opener = request.build_opener(proxy_hander)
    opener_list.append(opener)

import  random
url = "http://www.baidu.com"

try:
    opener = random.choice(opener_list)
    request.install_opener(opener)
    rsp = request.urlopen(url)
    print(rsp.read().decode())
except error.URLError as e:
    print(e)
except error.HTTPError as e:
    print(e)
except Exception as e:
    print(e)