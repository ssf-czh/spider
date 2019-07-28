'''
爬取包图网中的视频
下载MP4型的文件
'''
import requests
from lxml import etree
import os

class Spider():
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"}
        self.page = 1
    def start(self, url):
        rsp = requests.get(url, headers=self.headers)
        # print(rsp.text)
        html = etree.HTML(rsp.text)

        video_urls = html.xpath("//div[@class='media-list']//div[@class='video-play']/video/@src")
        # print(video_urls, len(video_urls))

        video_titles = html.xpath("//div[@class='media-list']//div[@class='show-image']/img/@alt")
        # print(video_titles, len(video_titles))

        print("正在打印第{}页".format(self.page))
        self.page += 1

        self.write_video(video_urls, video_titles)

    def write_video(self, urls, titles):

        path = 'G:\Git_Repository\spider\习题班\数据存储\\test\\aibao_video'
        if not os.path.exists(path):
            os.mkdir(path)
        for url, title in  zip(urls,titles):
            url = "http:" + url
            title = title + '.mp4'
            rsp = requests.get(url)
            with open(path +'\\' + title, "wb") as f:
                f.write(rsp.content)


if __name__ == '__main__':
    spider = Spider()
    spider.start("https://ibaotu.com/shipin/7-0-0-0-0-1.html")

