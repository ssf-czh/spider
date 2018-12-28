import requests
import re
import json
import time
def get_one_page(url):
   try:
       headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
       }
       rsp = requests.get(url, headers=headers)
       if rsp.status_code == 200:
           return rsp.text
       return None
   except Exception:
       return None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.'
        '*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )
    items = re.findall(pattern, html)
    # print(type(items))
    # print(items)
    for item in items:
        yield {
            "index": item[0],
            "image": item[1],
            "title": item[2],
            "action": item[3].strip()[3:],
            "time": item[4].strip()[5:],
            "score":item[5] + item[6]
        }
    # print(item[0])
def write_to_file(content):
    with open("result.txt","a",encoding= "utf-8") as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')

def main(offset):
    url = "http://www.maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
        time.sleep(1)
