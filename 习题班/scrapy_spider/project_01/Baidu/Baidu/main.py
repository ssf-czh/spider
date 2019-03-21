'''
可以不用dos命令模式
在这里进行命令操作
'''
from scrapy import cmdline


cmdline.execute("scrapy crawl Baidu_spider".split())