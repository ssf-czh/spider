'''
模拟豆瓣登入
user  = ssf-czh
passwd = 13107620755

url =  https://www.douban.com/
'''
from selenium import webdriver

drive = webdriver.Chrome()

drive.get("https://mail.163.com/")

drive.implicitly_wait(1)

print(type(drive.find_element_by_xpath("//iframe")),len(drive.find_element_by_xpath("//iframe")))
# drive.switch_to.frame(drive.find_element_by_xpath("//iframe"))

# drive.find_element_by_name("email").clear()
# drive.find_element_by_name("email").send_keys("sadasd")




# iframe = drive.find_element_by_tag_name("iframe")
# print(type(iframe))


#
# drive.switch_to.frame(drive.find_element_by_xpath("//iframe[@src='//accounts.douban.com/passport/login_popup?login_source=anony']"))
#
#
#
# # drive.find_element_by_class_name("account-tab-account on").click()

# drive.find_element_by_id("account-form-input").clear()
# drive.find_element_by_id("account-form-input").send_keys("ssf-czh")
# drive.find_element_by_id("password").clear()
# drive.find_element_by_id("password").send_keys("13107620755")
#
# drive.find_element_by_class_name("btn btn-account").click()
#
# with open("G:\Git_Repository\spider\习题班\selenium_\img\\test_02.html", "a", encoding="utf-8") as f:
#     f.write(drive.page_source)
