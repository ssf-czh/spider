import requests
# import  parser

params = {
    "czh": 19,
    "sex": "man"
}
r = requests.get("http://httpbin.org/get",params=params)
# r.text是str类型的 json格式 如果想解析返回结果得到一个字典的话，就要用到json方法
print(type(r.text))
print(r.json())
print(type(r.json()))