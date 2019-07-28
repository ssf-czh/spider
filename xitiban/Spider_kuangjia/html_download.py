'''
Html下载器：

'''

import requests

class HtmlDownload(object):
    def download(self,url):
        if url == None:
            return None
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        res = requests.get(url,headers=headers)

        if res.status_code == 200:
            # res.encoding = "utf-8"
            res.encoding = res.apparent_encoding
            return