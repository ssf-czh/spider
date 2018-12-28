from urllib import request

if __name__ == '__main__':
    url = "http://stock.eastmoney.com/news/1407,20170807763593890.html"

    rsp = request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Status:{0}".format(rsp.getcode()))