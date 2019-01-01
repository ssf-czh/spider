'''
模拟ajax爬取微博
评论 点赞 文本 转发 内容

'''

import requests
from pyquery import PyQuery as py

url = "https://m.weibo.cn/api/container/getIndex"

headers= {
    "Accept": "application/json, text/plain, */*",
    "MWeibo-Pwa": "1",
    "Referer": "https://m.weibo.cn/u/2830678474",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
def get_onepage(page):
    params = {
        "type": "uid",
        "value": "2830678474",
        "containerid": "1076032830678474",
        "page": page
    }
    try:
        rsp = requests.get(url=url, headers=headers, params=params)
        if rsp.status_code == 200:
            return rsp.json()
    except requests.ConnectionError as e:
        print("ERROR", e.args)
def parse_page(json):
    if(json):
        items = json.get("data").get("cards")
        for item in items:
            weibo = {}
            item = item.get("mblog")
            # print(type(item))
            # print(item)
            # print(item.get('id'))
            # print(item.get("id"))
            weibo["id"] = item["id"]
            weibo["text"] = py(item["text"]).text()
            weibo["attitudes"] = item["attitudes_count"]
            weibo["comments"] = item["comments_count"]
            weibo["reposts"] = item["reposts_count"]
            yield weibo

if __name__ == '__main__':
    for i in range(2,11):
        json = get_onepage(i)
        results = parse_page(json)
        # print(type(results))
        for result in results:
            print(result)


#
#
# def fun():
#     for i in range(10):
#         yield {2:3}
# f = fun()
# for i in f:
#     print(i)
#     print(i[2])