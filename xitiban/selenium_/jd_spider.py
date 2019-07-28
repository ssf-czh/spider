'''
利用selenium来爬取京东
并且把数据存到mongodb中
'''
from selenium import webdriver
import pymongo
from 习题班.数据存储.ApiDemo import MongoDB_API

# expected_condition as EC 是负责条件的发起 触发
from selenium.webdriver.support import expected_conditions as EC

'''
# 下面的引入的 作用： 设置等待
selenium主要提供隐性等待和显性等待
'''
from lxml import etree

from selenium.webdriver.support.ui import WebDriverWait

import time
#捕获超时异常
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

#启动浏览器
broswer = webdriver.Chrome()
wait = WebDriverWait(broswer, 50)

#连接数据库
# client = pymongo.MongoClient("localhost",27017)
# db = client.jd_computer
# collection = db.computer
mongo = MongoDB_API.MongoDB("localhost", 27017, "jd_computer", "computer")


def to_mongodb(data):

    #数据存储
    try:
        mongo.add(data)
        print("插入成功")
    except:
        print("插入失败")

def search():
    broswer.get("https://www.jd.com/")
    try:
        # 查找搜素框和搜素按钮 输入信息后点击
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#key")))
        submit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'button')))
        # print(input)
        input.send_keys("笔记本")
        submit.click()
        button_1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='f-sort']/a[2]/span")))
        button_1.click()
        page_num = wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='p-skip']/em/b")))
        return page_num.text

    except TimeoutException:
        search()
def spider():
    try:
        broswer.execute_script("window.scrollTo(0, document.documentElement.clientHeight);")
        time.sleep(5)
        broswer.execute_script("window.scrollTo(0, document.documentElement.clientHeight);")

        html = broswer.page_source
        # print(html)
        parse(html)

        print("*" * 20)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='p-num']/a[@class='pn-next']/em")))
        button.click()
        print("okkkkkkk")
    except:
        print("noooooo")

def parse(html):
    # print(html)
    html = etree.HTML(html)

    goods = html.xpath("//ul[@class='gl-warp clearfix']//li")
    print(len(goods))
    count = 1
    for good in goods:
        data={}
        price = good.xpath(".//div[@class='p-price']/strong/i/text()")[0]
        data["price"] = price
        title = good.xpath(".//div[@class='p-name p-name-type-2']/a/em/text()")[0]
        data["title"] = title
        # print(count,title,price)
        count = count + 1

        to_mongodb(data)

def main():
    page_number = search()
    for page in range(1,4):
        print("正在爬取第{}页".format(str(page)))
        html = spider()
        time.sleep(2)

if __name__ == '__main__':
    main()
    # data = {'price': '4199.00', 'title': '小米 (MI)Ruby 15.6英寸金属轻薄',"_id":1}
    # mongo.add(data)

