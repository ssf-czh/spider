'''
滑块验证码
哔哩哔哩 登录验证
'''
# from selenium.webdriver.common.action_chains import *
# from selenium import webdriver
# import time
# import random
# from PIL import Image
#
# patn = 'chromedriver.exe'
# browser = webdriver.Chrome(patn)
#
#
# # 获取偏移量
# def get_distance(image1, image2):
#     '''
#     拿到滑动验证码需要移动的距离
#     :param image1:没有缺口的图片对象
#     :param image2:带缺口的图片对象
#     :return:需要移动的距离
#     '''
#     threshold = 60
#     left = 60
#     for i in range(left, image1.size[0]):
#         for j in range(image1.size[1]):
#             rgb1 = image1.load()[i, j]
#             rgb2 = image2.load()[i, j]
#             res1 = abs(rgb1[0] - rgb2[0])
#             res2 = abs(rgb1[1] - rgb2[1])
#             res3 = abs(rgb1[2] - rgb2[2])
#             if not (res1 < threshold and res2 < threshold and res3 < threshold):
#                 print("到", i-7)
#                 return i - 7  # 经过测试，误差为大概为7
#     print("到", i - 7)
#     return i - 7  # 经过测试，误差为大概为7
#
#
# # 拿到移动轨迹
# def get_tracks(distance):
#     '''
#     拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
#     匀变速运动基本公式：
#     ①v=v0+at
#     ②s=v0t+½at²
#     ③v²-v0²=2as
#     :param distance: 需要移动的距离
#     :return: 存放每0.3秒移动的距离
#     '''
#     # 初速度
#     v = 0
#     # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
#     t = 0.3
#     # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
#     tracks = []
#     # 当前的位移
#     current = 0
#     # 到达mid值开始减速
#     mid = distance * 4 / 5
#
#     while current < distance:
#         if current < mid:
#             # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
#             a = 2
#         else:
#             a = -3
#
#         # 初速度
#         v0 = v
#         # 0.2秒时间内的位移
#         s = v0 * t + 0.5 * a * (t ** 2)
#         # 当前的位置
#         current += s
#         # 添加到轨迹列表
#         tracks.append(round(s))
#
#         # 速度已经达到v,该速度作为下次的初速度
#         v = v0 + a * t
#     return tracks
#
#
# # 鼠标模拟滑动,按照轨迹拖动，完全验证
# def move_slider(tracks):
#     ActionChains(browser).click_and_hold(slider).perform()
#     for track in tracks:
#         ActionChains(browser).move_by_offset(xoffset=track, yoffset=0).perform()
#     else:
#         ActionChains(browser).move_by_offset(xoffset=3, yoffset=0).perform()  # 先移过一点
#         ActionChains(browser).move_by_offset(xoffset=-3, yoffset=0).perform()  # 再退回来，是不是更像人了
#
#     time.sleep(0.5)  # 0.5秒后释放鼠标
#     ActionChains(browser).release().perform()
#
#
# if __name__ == '__main__':
#
#     try:
#         browser.get('https://passport.bilibili.com/login')
#         browser.save_screenshot('lodin.png')
#
#         username = browser.find_element_by_id('login-username')
#         password = browser.find_element_by_id('login-passwd')
#         # 获取滑块
#         slider = browser.find_element_by_xpath('//div[@id="gc-box"]/div/div[3]/div[2]')
#
#         print(slider)
#         username.send_keys('账号')
#         password.send_keys('密码')
#
#         # 鼠标悬停事件(显示完整图片)
#         ActionChains(browser).move_to_element(slider).perform()
#         time.sleep(1)
#         screenshot = browser.save_screenshot('tu1.png')
#
#         print(type(screenshot))
#
#         time.sleep(2)
#
#         # 鼠标点击(显示残缺图片)
#         slider.click()
#         time.sleep(3)
#         # browser.save_screenshot('tu2.png')
#         # img_1 = Image.open('tu1.png')
#         # img_2 = Image.open('tu2.png')
#         # img_1.show()
#         # img_2.show()
#
#
#         browser.close()
#         # 获取 图片的位置大小
#         img1 = browser.find_element_by_xpath(xpath='//div[@class="gt_cut_fullbg gt_show"]')
#         location = img1.location
#         size = img1.size
#         top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
#             'width']
#         print('图片的宽:', img1.size['width'])
#         print(top, bottom, left, right)
#
#         #  保存 裁剪 图片
#         img_1 = Image.open('tu1.png')
#         img_2 = Image.open('tu2.png')
#         img_1.show()
#         img_2.show()
#
#         capcha1 = img_1.crop((left, top, right, bottom))
#         capcha2 = img_2.crop((left, top, right, bottom))
#         capcha1.save('tu1-1.png')
#         capcha2.save('tu2-2.png')
#
#
#         # 获取验证码图片
#         img_11 = Image.open('tu1-1.png')
#         img_22 = Image.open('tu2-2.png')
#         img_11.show()
#         img_22.show()
#
#         distance = get_distance(img_11, img_22)
#
#         tracks = get_tracks(distance)
#         print(tracks)
#         print(distance, sum(tracks))
#         move_slider(tracks)
#     except:
#         pass
#






import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import tesserocr
from PIL import Image
from io import BytesIO
import math
user = "17605033617"
password =  "13107620755"
class log_in():
    def __init__(self):
        self.url = "https://passport.bilibili.com/login"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.user = user
        self.password = password
        # self.get_web()
        # self.input()

    def get_web(self):
        self.browser.get(self.url)
    def input(self):
        first = self.browser.find_element(By.ID, "login-username")
        second = self.browser.find_element(By.ID, "login-passwd")
        # user = input("输入账号：")
        # password = input("输入密码：")
        first.send_keys(user)
        second.send_keys(password)
    def get_button(self):
        '''
        获得滑动按钮
        :return: webelement类型的滑动按钮
        '''
        button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.gt_slider_knob")))
        return button
    def get_screenshot(self):
        '''
        获取网页截图
        :return: 截图对象
        '''
        screenshot = self.browser.get_screenshot_as_png()
        # print("---",type(screenshot))
        # print('666:', type(BytesIO(screenshot)))
        # open 需要打开一个路径或者一个文件
        # BytesIO是创建一个储存在文件内的二进制对象
        # open 放回一个pngimage对象
        screenshot = Image.open(BytesIO(screenshot))
        # screenshot = Image.open(screenshot)
        # screenshot.show()
        # print("!!!!",type(screenshot))
        return screenshot
    def get_position(self):
        '''
        获取验证码的位置
        :return: 验证码位置的元祖
        '''
        image = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gt_cut_fullbg")))
        time.sleep(0.5)
        # 标签对象的左上角位置
        location = image.location

        # image是个webelement标签对象
        # 这个标签在网页上占的长和宽
        size = image.size
        top, bottom, left, right = location["y"], location["y"] + size["height"], location["x"], location["x"] + size["width"]
        print(top+55, bottom+85, left+138, right+198)
        # 代表了验证码的具体左上到右下的元祖


        # image11 = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gt_box")))
        # time.sleep(0.5)
        # # 标签对象的左上角位置
        # location11 = image11.location
        #
        # # image是个webelement标签对象
        # # 这个标签在网页上占的长和宽
        # size11 = image11.size
        # top11, bottom11, left11, right11 = location11["y"]+size11["height"]*0.5 , location11["y"] + size11["height"]*1.5, location11["x"]+size11["width"]*0.5, location11["x"] + size11[
        #     "width"]*1.5
        # print(top11, bottom11, left11, right11)
        # return (top11, bottom11, left11, right11)
        # # 代表了验证码的具体左上到右下的元祖




        return (top+55, bottom+85, left+138, right+198)
    def get_image(self):
        '''
        获取验证码图像
        :return: 验证码图像对象
        '''
        top, bottom, left, right = self.get_position()
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        # print(type(captcha))
        # captcha.show()
        return captcha
    def is_equal(self,image1, image2, x, y):
        '''
        判断2个像素点是否相同
        :param image1: 完整图
        :param image2: 缺图
        :param x: 位置x
        :param y: 位置y
        :return: 是否相同
        '''
        p1 = image1.load()[x, y]
        p2 = image2.load()[x, y]
        fazhi = 60
        res1 = abs(p1[0] - p2[0])
        res2 = abs(p1[1] - p2[1])
        res3 = abs(p1[2] - p2[2])
        # print(res1, res2, res3, x, y)
        if(res1 < fazhi and res2 <fazhi and res3 < fazhi):
            return True
        else:
            print("x={0}, y = {1}".format(x, y))
            return False
    def get_gap(self, image1, image2):
        '''
        :param image1:
        :param image2:
        :return:
        '''
        # image1.show()
        # image2.show()
        print(type(image1.size))
        for i in range(image1.size[0]):
            for j in range(image1.size[1]):
                # print(image1.size[0]-1 - i - 30)
                if not self.is_equal(image1, image2, image1.size[0]-1 - i, j):
                    print("offset:", image1.size[0]-1 - i-95)
                    return  image1.size[0]-1 - i-95





    def get_track(self, distance):
        '''
        根据偏移量获取轨迹
        :param distance: 偏移量
        :return:
        '''
        track = [distance]
        ActionChains(self.browser).click_and_hold(self.get_button()).perform()
        ActionChains(self.browser).move_by_offset(xoffset=distance,yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()


    def log(self):
        # 申请网站
        self.get_web()
        # 用户输入
        self.input()
        button = self.get_button()
        # 移动到按钮处，让验证码出现
        ActionChains(self.browser).move_to_element(button).perform()
        time.sleep(0.5)
        # 获得原始验证码对象
        image1 = self.get_image()
        # image1.show()
        button.click()
        # 休息3秒防止出现错误提示
        time.sleep(3)
        # 获得需要验证的验证码
        image2 = self.get_image()
        # image2.show()
        # 获得需要偏移的量
        distance = self.get_gap(image1, image2)
        print(distance)
        # 移动
        self.get_track(distance)

        # self.browser.close()
        # r.browser.close()
if __name__ == '__main__':
    r = log_in()
    r.log()
