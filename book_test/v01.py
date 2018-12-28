from urllib import request,parse

data = bytes(parse.urlencode({"word":"hello"}),encoding="utf-8")
rsp = request.urlopen("http://httpbin.org/post",data= data)
print(rsp.read())
