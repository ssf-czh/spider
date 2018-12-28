from urllib import request,error,parse
from http import cookiejar

cookie = cookiejar.LWPCookieJar()
cookie.load("cookie.txt",ignore_discard=True, ignore_expires=True)
handler_cookie = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(handler_cookie)

rsp = opener.open("http://www.baidu.com")
print(rsp.read().decode())
