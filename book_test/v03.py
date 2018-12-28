from http import cookiejar
from urllib import error,request

if __name__ == '__main__':
    cookie = cookiejar.CookieJar()
    hander = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(hander)
    request.install_opener(opener)
    try:
        rsp = opener.open("http://www.baidu.com")
        # rsp = request.urlopen("http://www/baidu.com")
        print(cookie)
        for item in cookie:
            print(item.name + "="+item.value)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

# from urllib import request,error
# from http import cookiejar
#
# cookie = cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
#
# rsp = opener.open("http://www.baidu.com")
# for item in cookie:
#     print(item.name +"="+item.value)