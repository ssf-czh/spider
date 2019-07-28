from 习题班.Spider_kuangjia.Data_in import Data_in
from 习题班.Spider_kuangjia.Html_parse import Html_parse
from 习题班.Spider_kuangjia.url_manage import UrlManager
from 习题班.Spider_kuangjia.html_download import HtmlDownload

class SpiderMain(object):
    def __init__(self):
        self.manager = UrlManager()
        self.download = HtmlDownload()
        self.parse = Html_parse()
        self.datain = Data_in()

    def crawl(self,root_url):
        '''
        添加入口url地址
        :param root_url:入口url
        :return:
        '''
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url地址 同时判断抓取了多少个url地址
        while(self.manager.has_new_url() and self.manager.old_urls < 100):
            try:
                #从url地址中获取新的url地址
                new_url = self.manager.get_new_url()
                #Html下载器进行页面下载
                html = self.download.download(new_url)
                #将html进行解析
                new_urls,data = self.parse.parse(new_url, html)
                #将获取到的urk地址添加到url管理器中
                self.manager.add_new_urls(new_urls)
                #进行数据存储
                self.datain.store_data(data)

                print("已抓取{}个链接".format(self.manager.old_url_size()))
            except Exception as e:
                print("fail ",e)

if __name__ == '__main__':
    url = "http+**********"
    spider_main = SpiderMain()
    spider_main.crawl(url)