'''
利用selenium爬取淘宝中的商品信息
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KEYWORD = "iPad"

import pymongo
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from urllib.parse import quote
import time
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'

KEYWORD = 'ipad'

MAX_PAGE = 100

SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
# browser = webdriver.Chrome()
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-serve=127.0.0.1.8080')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        cookies ="miid=740529142264345084; cna=LSdJEzFnslECAdpqkRDdhgvG; thw=cn; t=930733cda517d0729817f983eef43090; v=0; cookie2=1202d4e8efdae16a8e687fa1174e5fcc; _tb_token_=e59deee13d781; unb=3328864018; sg=%E7%96%AF86; _l_g_=Ug%3D%3D; skt=fc3b7e24545064cc; cookie1=U7SjZQG23Iwba5lMH7jXNd%2BWzuio15PZqmw6tOMA8TM%3D; csg=cfbabb73; uc3=vt3=F8dByRIttvQOQqCly6A%3D&id2=UNN%2F5Ot8SsRQwA%3D%3D&nk2=tPEAlkxiOuIEWw%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; existShop=MTU0NjUxNTYzMg%3D%3D; tracknick=%5Cu6700%5Cu7231%5Cu5341%5Cu4E09%5Cu75AF; lgc=%5Cu6700%5Cu7231%5Cu5341%5Cu4E09%5Cu75AF; _cc_=VFC%2FuZ9ajQ%3D%3D; dnk=%5Cu6700%5Cu7231%5Cu5341%5Cu4E09%5Cu75AF; _nk_=%5Cu6700%5Cu7231%5Cu5341%5Cu4E09%5Cu75AF; cookie17=UNN%2F5Ot8SsRQwA%3D%3D; tg=0; enc=a%2BpoifS%2FIivqeRF46Eg2xHhulmWS5c3ZIDu%2BUblmFLtGS%2FXvTZKLcijQWCRCOluBp2l3htpER%2FkMBZMm0GNHXQ%3D%3D; mt=ci=18_1; hng=CN%7Czh-CN%7CCNY%7C156; swfstore=304077; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=E438CBECCE1298477056BBD6AC2C4496; uc1=cookie14=UoTYMD71YSiSSg%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D; l=aB71p3qxyuPwEUCKQManrsvjFOq5z0BPnVcW1Mwm8Tx4bW5BDjCL1F-dM_wINEIF8rzFu8mg505j0; isg=BEVFtCMuteq7i5E05JWeQzBiVIHTG6JcLD6Uf0epyX3x3mdQD1KQZeL07GKNnhFM; whl=-1%260%260%261546520924631"
        # browser.add_cookie(cookies)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')

def log_in():
    browser.get("https://login.taobao.com")
    # browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a').click()
    # # browser.find_element(By.CSS_SELECTOR, ".forget-pwd").click()
    # browser.find_element(By.ID,"TPL_username_1").send_keys("123")
    # browser.find_element(By.ID,"TPL_password_1").send_keys("456")
    # # browser.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[2]/div[3]/form/div[2]/span').click()
    # time.sleep(3)
    # dragger = browser.find_element(By.ID,"nc_1_n1z")
    # action = ActionChains(browser)
    # #
    # # for index in range(500):
    # #     try:
    # #         action.drag_and_drop_by_offset(dragger,500,0).perform()
    # #     except UnexpectedAlertPresentException:
    # #         break
    # #     time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, ".J_Quick2Static").click()


def main():
    log_in()
    # """
    # 遍历每一页
    # """
    # for i in range(1, MAX_PAGE + 1):
    #     index_page(i)
    # browser.close()
    # browser.get("https://www.baidu.com")
    # input = browser.find_element(By.CSS_SELECTOR,".s_ipt")
    # print(input)
    # input.send_keys("123")


if __name__ == '__main__':
    main()