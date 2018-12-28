'''
访问一个网址
设置user-agent进行伪装
'''
from urllib import request,error
if __name__ == '__main__':
    url = "http://www.baidu.com"

    try:
        # 第一种：
        # headers={}
        # headers["User-Agent"]= "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
        # req = request.Request(url, headers=headers)

        # 第二种：
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36")

        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
    print("done......")
