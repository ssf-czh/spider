'''
爬取酷狗top500
利用MongoDB进行数据存储
zip：https://www.cnblogs.com/xuchunlin/p/6676304.html
'''
import requests
import pymongo
from lxml import etree
from bs4 import BeautifulSoup

def kugou_spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    rsp = requests.get(url, headers=headers)
    # print(rsp.text)
    soup = BeautifulSoup(rsp.text, 'lxml')
    ranks = soup.select("span.pc_temp_num")
    titles = soup.select("a.pc_temp_songname")
    # print(title)
    song_times = soup.select("span.pc_temp_time")
    # print(song_times)
    for rank, title, song_time in zip(ranks, titles, song_times):
        date = {
            "rank": rank.get_text().strip(),
            "song": title.get_text().split("-")[-1].strip(),
            "singer": title.get_text().split("-")[0].strip(),
            "song_time": song_time.get_text().strip(),
            # print(rank, song, singer, song_time)
        }
        print(date)
        to_mongodb(date)
def to_mongodb(date):
    client = pymongo.MongoClient(host="localhost", port=27017)
    # print(client)
    songs = client.kg_songs.songs
    id = songs.insert_one(date).inserted_id
    print(id)

if __name__ == "__main__":
    urls = ["https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(str(i)) for i in range(1, 24)]
    # print(urls)
    for url in urls:
        kugou_spider(url)
