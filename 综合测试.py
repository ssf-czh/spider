'''
首先先找到 登入入口 - 先切到登入界面随便输入 切换模式查看请求
然后通过必要的headers和form //注意要用post方法

实验用requests 访问 http://www.jobbole.com/
1：实验 带cookie的请求头headers 是否可以直接登入账户  得出结论：可以 并且每登入退出一次 cookie就会变一次 所以需要手动再改变headers的cookie
2：实验 s = requests.Session()  s是否会保存 cookie 即保持会话状态 结论：会保持后端给的cookie 并且访问的时候会自动把cookie带到headers
'''
import requests
import json
# from urllib import parse
#
# # url = "https://movie.douban.com/j/chart/top_list"
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
# # url = "http://httpbin.org/get"
# params = {
#     "type": "11",
#     "interval_id": "100%3A90",
#     "action": "",
#     "start": "",
#     "limit": 20
# }
# # https://movie.douban.com/j/chart/top_list?
# # url = url + parse.urlencode(params)
# print(url)
# rsp = requests.get(url= url)
# # rsp = requests.get(url)
# print


#
# import requests
#
# url = "http://httpbin.org/cookies/set/number/123456789"
# u = "http://httpbin.org/cookies"
# s = requests.Session()
# s.get(url)
# r = s.get(u)
#
# print(r.text)


from urllib import request, error, parse
from http import cookiejar
import requests
import json
s = requests.Session()
def log_in():
    url = "http://www.jobbole.com/wp-admin/admin-ajax.php"
      # url = "http://date.jobbole.com/wp-login.php"

    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
            "Connection": "keep-alive"
    }
    data = {
        "action": "user_login",
        "user_login": "augsnano",
        "user_pass": "123456789",
        "remember_me": "1",
        "redirect_url": "http://www.jobbole.com/"
    }

    rsp = s.post(url = url, data = data, headers = headers)
    print(rsp.cookies)
    # print(rsp.status_code)
    # print(rsp.text)

def home_page():
    url = "http://www.jobbole.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "Connection": "keep-alive"
    }

    rsp = s.get(url, headers = headers)
    print(rsp.text)
if __name__ == '__main__':

    # login()
    log_in()
    home_page()










    #
    # url = "http://www.jobbole.com/"
    # #
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
    #     "Connection": "keep-alive",
    #     "Cookie": "PHPSESSID=q42dvi7sc7cf4c9ipk3sn237v5; wordpress_test_cookie=WP+Cookie+check; wordpress_logged_in_0efdf49af511fd88681529ef8c2e5fbf=augsnano%7C1548423390%7CZejbFmy2X3lkfrYaHoObIKd18mddzIK9ShafeNERNZw%7C80a0fbfa92fc34fe6934bf885d8c7d83e87462cce53e3605501fb23dfd36264f"
    # }
    # rsp = requests.get(url,headers =headers)
    # print(rsp.text)

