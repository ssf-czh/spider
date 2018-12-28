from urllib import request,parse
'''
掌握对url进行参数编码的方法
需要使用parse模块
'''

if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    wd=input("输入你的关键字:")

    # 想使用数据，就一定要使用字典结构
    qs={
        "wd":wd
    }
    qs = parse.urlencode(qs)

    fullurl =url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)

    html = rsp.read()

    html = html.decode()

    print(html)

