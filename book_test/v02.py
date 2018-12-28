from urllib import parse,request
url = "http://httpbin.org/post"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
    "Host":"httpbin.org"
}
dict = {
    "name":"gereny"
}
data = bytes(parse.urlencode(dict),encoding="utf-8")
rqs = request.Request(url=url,data=data,headers=headers,method="POST")
rsp = request.urlopen(rqs)
print(rsp.read().decode())