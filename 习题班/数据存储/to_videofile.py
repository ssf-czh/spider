
# with open(filename,"wb") as f:
#     f.wirte(content)
'''
音频文件的存储
二进制
1:获取下载文件的url 二进制方式 下载
urllib ，模块提供的request.urlretrieve() 此模块可以进行音频文件下载
        也支持将远程数据下载到本地
def urlretrieve(url, filename=None, reporthook=None, data=None):
url:我们下载的url地址
filename:数据存储路径_+文件名
reporthook:要求回调函数。：连接到服务器或者相应数据传输下载完毕时触发该回调函数
            显示当前的下载进度
data：(filename，headers)元祖

'''
from urllib import request
import os,requests
from lxml import etree
def f(a,b,c):
    '''

    :param a:已经下载的数据块
    :param b: 每个数据块的大小
    :param c: 总的数据块大小*每个数据块的大小
    :return: a*b/c就是下载百分比
    '''
    per = a * b /c *100.0
    if(per >= 100):
        per = 100
    print("已经下载{}".format(per))
def tiantang_spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    rsp = requests.get(url,headers = headers)
    # print(rsp.text)
    html = etree.HTML(rsp.text)
    img_urls = html.xpath("//div[@class='il_img']//img/@src")
    dir = "animal_img"
    if not os.path.exists(dir):
        os.mkdir(dir)
    for img_url in img_urls:
        # print(img_url,type(img_url))
        filename = img_url.split("/")[-1]
        request.urlretrieve(url= img_url,filename = dir + "\\" + filename,reporthook=f)



if __name__ == "__main__":
    url = "http://www.ivsky.com/bizhi/dongwu/"
    tiantang_spider(url)



