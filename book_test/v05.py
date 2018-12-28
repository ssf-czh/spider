'''
抓取二进制数据
比如图片，音频
'''
import requests

rsp = requests.get("http://github.com/favicon.ico")
print(rsp.text)
print(rsp.content)

with open("05.ico","wb") as f:
    f.write(rsp.content)