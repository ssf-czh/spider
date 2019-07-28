'''
利用selenium运行js脚本语言
'''
from selenium import webdriver

driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com")

# 运行让输入框边变成红色的脚本
js = 'var j=document.getElementById("kw");j.style.border="2px solid red"'

# 调用搜索输入框的脚本
driver.execute_script(js)
driver.implicitly_wait(2)

# 截图
driver.save_screenshot("G:\Git_Repository\spider\习题班\selenium_\img\\red_input.jpg")

