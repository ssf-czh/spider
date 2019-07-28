'''
爬取拉勾网信息
利用pandas 可视化
直接用www.lagou.com免登入
'''
import requests

def lagou_spider(page):
    data = {
        "first": "false",
        "pn": str(page),
        "kd": "python",
    }
    headers = {
        "Connection": "keep-alive",
        "Content-Length": str(len(data)),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Host": "www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_python?city=%E7%A6%8F%E5%B7%9E&cl=true&fromSearch=true&labelWords=&suginput="
    }
    rsp = requests.post(url='https://www.lagou.com/jobs/positionAjax.json?city=%E7%A6%8F%E5%B7%9E&needAddtionalResult=false', headers=headers, data=data)
    print(rsp.status_code)
    print(rsp.text)

if __name__ == '__main__':
    for page in range(1,2):
        lagou_spider(page)