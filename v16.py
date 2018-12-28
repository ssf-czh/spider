from urllib import request
import  ssl
url = "https://www.12306.cn/mormhweb"
rsp = request.urlopen(url)

print(rsp.read().decode())