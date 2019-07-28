'''
爬取博客园python专栏的文章 、文章作者、发布时间、评论以及阅读数
使用BeatifulSoup进行数据解析
'''
import requests
from bs4 import BeautifulSoup

def cnblogs_spider(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    rsp = requests.get(url,headers= headers)
    print(rsp.text)
    soup = BeautifulSoup(rsp.text,"lxml")
    items = soup.select("div[class='post_item']")
    # print(body)
    for item in items:
        # 获取文章名字
        title = item.select("div h3 a[class='titlelnk']")[0].string
        print("文章标题: ", title)
        # 获取文章链接
        href = item.select("div h3 a[class='titlelnk']")[0]["href"]
        print("文章链接： ", href)
        # 获取文章内容
        content = item.select("p[class='post_item_summary']")[0].get_text()
        print("文章内容： ", content)
        # 获取文章的作者
        author = item.select("div a[class='lightblue']")[0].string
        print("文章作者：", author)
        # 获取文章作者的主页
        author_home = item.select("div a[class='lightblue']")[0]["href"]
        print("author_home:",author_home)

        # 获取时间和评论和阅读量
        div = item.select("div[class='post_item_foot']")[0].get_text()
        data = div.split(" ")
        # print(data)
        # ['\n陈彦斌', '\r\n', '', '', '', '发布于', '2019-02-04', '15:53', '\r\n', '', '', '', '\r\n', '', '', '', '', '', '',
        #  '', '评论(0)阅读(4)']
        # 获取时间
        time = data[6]+" "+data[7]
        print("文章发布时间： ", time)
        # 获取评论数
        comment = data[-1].lstrip("评论(").split(")")[0]
        print("评论数： ", comment)
        # 获取阅读数
        read_times =data[-1].split("(")[-1].rstrip(")")[0]
        print("阅读量： ", read_times)



        print("***"*20)
if __name__ == "__main__":
    url = "https://www.cnblogs.com/cate/python/"
    cnblogs_spider(url)