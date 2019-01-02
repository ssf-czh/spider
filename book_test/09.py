import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# '''
# Selenium的基本综合使用
# '''
# browser = webdriver.Chrome()
# try:
#     browser.get("http://www.baidu.com")
#     input = browser.find_element_by_id("kw")
#     input.send_keys("python")
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser,10)
#     wait.until(EC.presence_of_element_located((By.ID,"content_left")))
#     print(browser.current_url)
#     print(browser.get_cookies)
#     print(browser.page_source)
# finally:
#     browser.close()


'''
访问淘宝页面
'''
# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# print(browser.page_source)
# browser.close()


'''
访问淘宝并且查找html中的结点
'''
# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# # input_first = browser.find_element_by_id("q")
# # input_second = browser.find_element_by_css_selector("#q")
# # input_third = browser.find_element_by_xpath("//*[@id='q']")
# # 第二种方法 简易
# # input_first = browser.find_element(By.ID,"q")
# # print(input_first,input_second,input_third)
# # print(input_first,input_second)
#
# lis = browser.find_elements(By.CSS_SELECTOR, ".service-bd li")
# print(lis)
# browser.close()



'''
结点交互
常见：输入文字：send_keys()
        清空文字：clear()
        点击：click()
'''

# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# input = browser.find_element(By.ID,"q")
# input.send_keys("iPhone")
# time.sleep(1)
# input.clear()
# input.send_keys("iPad")
# button = browser.find_element(By.CLASS_NAME, "btn-search")
# button.click()

'''
动作链
结点交互是针对结点（标签）执行的
对于不是特定结点的动作 比如鼠标拖拽 键盘按键 就是动作链
'''
# 实现一个结点的拖拽
# from selenium.webdriver import ActionChains
# browser = webdriver.Chrome()
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame("iframeResult")
# source = browser.find_element(By.ID, "draggable")
# target = browser.find_element(By.ID, "droppable")
# action = ActionChains(browser)
# action.drag_and_drop(source, target)
# action.perform()

'''
直接利用 selenium执行js代码
比如下拉进度条，可以直接模拟js代码
调用execute_script()
'''

# browser = webdriver.Chrome()
# browser.get("https://www.zhihu.com/explore")
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# browser.execute_script("alert('To Bottom')")


'''
获取结点信息

通过browser.page_source 可以获得网页的源代码 然后就可以用解析库 来提取信息
但是sele 也提供了寻找结点的方法（find_element(By.)）
所以可以直接获得webelement对象的结点 直接调用其属性和方法来获取结点信息
'''

# browser = webdriver.Chrome()
#
# browser.get("https://www.zhihu.com/explore")
# logo = browser.find_element(By.ID, "zh-top-link-logo")
# print(logo)
# # print(logo.get_attribute("class"),logo.text)
# input = browser.find_element(By.CLASS_NAME, "zu-top-add-question")
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)
# print(input.text)

'''
切换frame
frame 是页面中的页面
有个结点叫做iframe 是内页面的标志
如果在一个外页面调用find_element方法寻找内页面的结点 是找不到的
只有将browser切换到内页面才能寻找的到
同理 外面的结点只能切换到外页面才能找的到
'''

# browser = webdriver.Chrome()
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame("iframeResult")
# try:
#     logo = browser.find_element(By.CLASS_NAME,"logo")
# except Exception as e:
#     print("ERROR")
# browser.switch_to.parent_frame()
# logo = browser.find_element(By.CLASS_NAME,"logo")
# print(logo, logo.text)


'''
延时等待：
sele中 由于模仿浏览器运行
所以如果直接用page_source方法 可能并不是浏览器完全加载后的数据，比如ajax
所以我们需要等待一定时间 确保结点已经加载出来
隐式等待不提倡使用
显式等待
要查找一个结点，指定最长等待时间 如果规定时间内加载出来这个结点 就返回
否则抛出异常 

'''
#
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# wait = WebDriverWait(browser,10)
# # 如果10s内ID为q的结点加载出来就返回
# input = wait.until(EC.presence_of_element_located((By.ID,"q")))
# # 如果10s内属性为btn-search的结点是可点击的 就返回
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".btn-search")))
# print(input,button)

'''
前进和后退
'''
# browser = webdriver.Chrome()
# browser.get("https://www.baidu.com")
# browser.get("https://www.taobao.com")
# browser.back()
# time.sleep(1)
# browser.forward()
# time.sleep(1)
# browser.close()


'''
通过selenium 可以队cookie 进行很方便的操作
获得cookie 增加cookie 删除cookie
'''
#
# browser = webdriver.Chrome()
# browser.get("https://www.zhihu.com/explore")
# print(browser.get_cookies())
# browser.add_cookie({"name": "name", "domain": "www.zhihu.com", "value": "sasagermey"})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

'''
选型卡管理：
就是一个浏览器打开多个网页
'''

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get("https://www.taobao.com")
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get("https://www.python.org/")