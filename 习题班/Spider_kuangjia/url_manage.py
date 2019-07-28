'''
url管理器(类)：
变量：
    -已经爬取的url集合
    -还没爬取的url集合
基本函数：
1:判断是否还有未爬取的url has_new_url()
2：添加新的url到未爬取的url集合 add_new_url()
3：获得一个未爬取的url get_new_url()
4：获得未爬取url集合的大小 new_url_size()
5：获得已爬取的url集合大小 old_url_size()

'''


class UrlManager(object):
    def __init__(self):
        self.new_urls = set() #未爬取的url集合
        self.old_urls = set() #已爬取的url集合
    def has_new_url(self):
        '''
        判断是否有未爬取的url地址
        :return:
        '''
        return self.new_urls_size()

    def get_new_url(self):
        '''获取一个未爬取的url'''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)
    def new_url_size(self):
        '''判断未爬的数目'''
        return len(self.new_urls)

    def old_url_size(self):
        '''返回已爬的数目'''
        return len(self.old_urls)




