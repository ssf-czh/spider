# 导入webdrive
from selenium import webdriver
# 如果想按键盘需要导入keys包
from selenium.webdriver.common.keys import Keys
import time

# 创建浏览器对象 excutable_path 指定路径 如果没有加入环境变量
# drive = webdriver.PhantomJS()


# get方法
# drive.get("https://www.baidu.com")
# 截图
# drive.save_screenshot("G:\Git_Repository\spider\习题班\selenium_\img\\baidu.png")
# 打印网页名字
# print(drive.title)

# 选择输入框 id=kw
# drive.find_element_by_id("kw").send_keys("美女")

# 点击确定按钮 id = 'su'
# drive.find_element_by_id("su").click()

# time.sleep(2)

# 截图
# drive.save_screenshot("G:\Git_Repository\spider\习题班\selenium_\img\\meinv.png")

# 打印源码信息
# print(drive.page_source)


# 打印cookie信息
# print(drive.get_cookies())

# 清空操作
# drive.find_element_by_id("kw").clear()

# drive.save_screenshot("G:\Git_Repository\spider\习题班\selenium_\img\\t1.png")

# 打印当前的url地址
# print(drive.current_url)
