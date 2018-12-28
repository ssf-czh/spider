from urllib import request
'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''
if __name__ == '__main__':
    url = "http://jobs.zhaopin.com/195435110251173.htm?ssidkey=y&ss=409&ff=03&sg=2644e782b8b143419956320b22910c91&so=1"
    # 打开相应url并把页面作为返回结果
    rsp = request.urlopen(url)
    # 返回的是一个字节流
    html = rsp.read()
    print(type(html))

    # 把字节流进行解码
    html = html.decode()
    print(html)