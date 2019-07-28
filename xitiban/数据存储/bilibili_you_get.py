'''
利用you-get下载b战视频
首先通过火狐浏览器获得每一页的json文件 其中包括了每个视频的详细url地址
https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&search_type=video&highlight=1&keyword=%E8%A7%86%E9%A2%91&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.2&page=2&single_column=0&callback=__jp0
最后一个参数没用 删除
https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&search_type=video&highlight=1&keyword=%E8%A7%86%E9%A2%91&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.2&page=2&single_column=0
'''
import requests
import os

def get_json(page):
    url = "https://api.bilibili.com/x/web-interface/search/type?jsonp=jsonp&search_type=video&highlight=1&keyword=%E8%A7%86%E9%A2%91&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.2&page={}&single_column=0".format(page)
    headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    rsp = requests.get(url=url, headers=headers)
    # rsp.encoding = rsp.apparent_encoding
    datas = rsp.json()
    dt = []
    for data in datas["data"]["result"]:
        dt.append((data["title"], data["arcurl"]))
    # print(dt)
    return dt
def down_load(data):
    path = r"G:\Git_Repository\spider\习题班\数据存储\bili_video"
    if not os.path.exists(path):
        os.mkdir(path)
    for title, url in data:
        filename = path + "\\" + title
        print("正在下载{}".format(title))
        os.system("you-get -o {} {}".format(filename, url))
        print("下载完成{}".format(title))

if __name__ == '__main__':
    for page in range(1,2):
        data = get_json(page)
        down_load(data)