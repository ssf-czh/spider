import json,requests
from bs4 import  BeautifulSoup

# str = '[{"username":"dachong", "age":"18"}]'
# print(type(str))
# json_str = json.dumps(str, ensure_ascii=False)
# print(json_str, type(json_str))
#
# new_str = json.loads(str)
# print(new_str,type(new_str))
#
# with open("temp.json","w") as f:
#     json.dump(json.loads(str),fp=f,indent=4)
# # sss=[]
# # with open("temp.json","r") as f:
# #     sss=json.load(f)
# # print(sss)
# https://blog.csdn.net/anthony_1223/article/details/82259286

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
rsp = requests.get("http://www.seputu.com/",headers = headers)
rsp.encoding = rsp.apparent_encoding
# print(rsp.text)
soup = BeautifulSoup(rsp.text, "lxml")
content = []
mulus = soup.find_all(class_= "mulu")
# print(len(items))
for mulu in mulus:
    # 标题
    big_title = mulu.find(name = "h2")

    if big_title !=None:
        big_title = big_title.string
        list = []
        # print(title)
        for a in mulu.find(class_= "box").find_all("a"):
            href = a.get("href")
            small_title = a.get("title")
            print(href,small_title)
            list.append({"href":href,"small_title":small_title})
        content.append({"big_title": big_title,"content": list})
# print(content)
# str_content = str(content)
# print(type(str_content))
with open("gcd.json", "a", encoding="utf-8") as f:
    json.dump(content,fp=f,ensure_ascii=False,indent=4)