'''
爬取虎扑论坛
并且写入mongodb中

要求：
格式清晰
自己写一个包 ：关于mongodba API的类
'''
import requests
from bs4 import BeautifulSoup
from 习题班.数据存储.ApiDemo import MongoDB_API


def hp_spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    rsp = requests.get(url, headers=headers)
    # print(rsp.text)
    return rsp.text

def parse(html):
    html = BeautifulSoup(html, "lxml")
    titles = html.select("div[class='titlelink box'] a[class='truetit']")
    hrefs = html.select("div[class='titlelink box'] a[class='truetit']")
    authors = html.select("div[class='author box'] a[class='aulink']")
    times = html.select("div[class='author box'] a[style='color:#808080;cursor: initial; ']")
    comments_reads = html.select("span[class='ansour box']")
    last_commnets = html.select("div[class='endreply box'] a")

    titles = [title.get_text().split("]")[-1] for title in titles]
    hrefs = ["https://bbs.hupu.com" + href["href"] for href in hrefs]
    authors = [author.get_text() for author in authors]
    times = [time.get_text() for time in times]
    comments_reads = [comment_read.get_text() for comment_read in comments_reads]
    comments = [item.split("\xa0/\xa0")[0] for item in comments_reads]
    reads = [item.split("\xa0/\xa0")[1] for item in comments_reads]
    last_commnets = [last_commnet.get_text() for last_commnet in last_commnets]

    return zip(titles, hrefs, authors, times, comments, reads, last_commnets)
    # print(titles,len(titles))
    # print(hrefs, len(hrefs))
    # print(authors,len(authors))
    # print(times, len(times))
    # print(comments, len(comments))
    # print(reads,len(reads))
    # print(last_commnets, len(last_commnets))
def to_mongo(data):
    table = MongoDB_API.MongoDB("localhost", 27017, "hupu_football", "athelete_mardia")
    for title, href, author, time, comment, read, last_commnet in data:
        table.add(
            {
                "title": title,
                "href": href,
                "author": author,
                "time": time,
                "comment": comment,
                "read": read,
                "last_commnet": last_commnet,
                "last_commnet": last_commnet
            }
        )




def main():
    urls = ["https://bbs.hupu.com/atleticodemadrid-{}".format(str(i)) for i in range(1, 11)]
    for url in urls:
        html = hp_spider(url)
        data = parse(html)
        to_mongo(data)



if __name__ == '__main__':
    main()