'''
使用csv存储数据
并且使用xpath来提取数据
'''
import requests
import csv
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
rsp = requests.get("http://www.seputu.com/",headers = headers)
rsp.encoding = rsp.apparent_encoding
html = etree.HTML(rsp.text)

div_mulus = html.xpath("//div[@class='mulu']")
rows = []
for div_mulu in div_mulus:
    big_title = div_mulu.xpath("./div[@class='mulu-title']/center/h2/text()")
    if len(big_title):
        small_div = div_mulu.xpath("./div[@class='box']/ul//li//a")
        # print(type(small_div))
        for div in small_div:
            href = div.xpath("./@href")[0]
            small_title = div.xpath("./@title")[0]
            # print(href,small_title)
            split_= small_title.split("]")
            time = split_[0]+']'
            small_title = split_[1]
            # print(big_title,small_title,href,time)
            content = [big_title,small_title,href,time]
            rows.append(content)
header = ['big_title','small_title',"small_title","href","time"]

with open("xpath_gcd_csv.csv","w",newline="") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(rows)



