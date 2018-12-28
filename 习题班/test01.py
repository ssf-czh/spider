'''
爬取百度贴吧
1 张继科吧主页是 https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=0
2.进去之后有很多页
    第二页网址是：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=50
    第三页网址是：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=100
    第四页的网址是：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=150
    ...
    ...
3 每一页在pn上加50 就是 0+i*50

解决方法：
    1.准备构建字典吗
        字典包括三部分 kw ie pn
    2 使用parse构建完整url
    3 使用for循环下载
'''
from urllib import  request,parse
if __name__ == '__main__':
    qs={
        "kw": "张继科",
        "ie": "utf-8",
        "pn": 0
    }
    # 2 使用parse构造完整url
    urls =[]
    baseurl = "http://tieba.baidu.com/f?"
    for i in range(10):
        pn = i*50
        qs["pn"]=str(pn)
        # 把qs转成字符串后和url拼接
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)
    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(url)
        print(html)