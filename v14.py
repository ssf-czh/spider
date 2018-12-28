from urllib import request,error,parse
from http import cookiejar
filename = "cookie.txt"
cookie = cookiejar.LWPCookieJar(filename=filename)

handler_cookie = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(handler_cookie)

opener.open("http://www.baidu.com")

cookie.save()