'''
爬取喜马拉雅音乐（类型首页中包含每个歌单的albumId 点击一个歌单会携带albumId信息 然后点击播放键自动传入Id信息 返回歌曲）

使用request.urlretrive 下载

pypinyin ： 把汉字准换成纯拼音

1:首先获取首页的html
2:由于要进入每个歌单 分析每个歌单的地址
https://www.ximalaya.com/yinyue/3595841/
https://www.ximalaya.com/yinyue/261506/
发现区别在于最后 但是最终目标在于获得音乐的url地址

发现此网站是通过js 点击事件获得数据 所以在抓包过程中点击播放键可以发现有请求发送
https://www.ximalaya.com/revision/play/album?albumId=261506&pageNum=1&sort=-1&pageSize=30
https://www.ximalaya.com/revision/play/album?albumId=3595841&pageNum=1&sort=-1&pageSize=30
放回的试json格式 里面包含了歌单里所有音乐信息

发现区别 在于albumId  推测出alblumId的是在首页的html中 所以可以在首页的html中查找albumId

'''
import pypinyin
import requests, re
import json
from urllib import request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
}


def music_spider(url):
    print(url)
    rsp = requests.get(url, headers=headers)
    # print(rsp.status_code)
    # print(rsp.text)
    return rsp.text

def get_albumId(html):
    # {"albumId": 261506, "title": "一段话 一首歌",
    albumIds = re.findall('"albumId":(.*?),', html)
    return albumIds[0] #如果需要全部直接返回 这里只爬取一个歌单
def main_download(id):
    url = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum=1&sort=-1&pageSize=30".format(id)
    rsp = requests.get(url, headers=headers)
    print(rsp.text)
    music_json = json.loads(rsp.text)
    music_items = music_json["data"]["tracksAudioPlay"]
    down_music(music_items)

def down_music(items):
    for item in items:
        title = item['trackName']
        src = item['src']
        print("正在下载{}".format(title))
        request.urlretrieve(url=src, filename=r'G:\Git_Repository\spider\习题班\数据存储\test\ximalaya_music' + '\\' +title + '.m4a')

if __name__ == '__main__':
    # tpe = input("请输入你想要的类型：")
    tpe ="流行"
    tpe = "".join(pypinyin.lazy_pinyin(tpe))
    url = 'https://www.ximalaya.com/yinyue/{}/'.format(tpe)
    html = music_spider(url)
    albumId = get_albumId(html)
    main_download(albumId)