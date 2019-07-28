'''
利用pandas numpy包进行数据分析
爬取中国票房 http://www.cbooo.cn/year?year=2018
利用bs4
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
def movies_spider(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    rsp = requests.get(url, headers=headers)
    # print(rsp.text)
    soup = BeautifulSoup(rsp.text, "lxml")
    movies = soup.find_all("tr")#获取囊括所有信息的大标签
    print(type(movies), len(movies))
    movie_name = [movie.find_all("td")[0].a["title"] for movie in movies[1:]]
    print(movie_name)
    movie_href = [movie.find_all("td")[0].a["href"] for movie in movies[1:]]
    print(movie_href)
    movie_type = [movie.find_all("td")[1].string for movie in movies[1:]]
    print(movie_type)
    movie_money = [movie.find_all("td")[2].string for movie in movies[1:]]
    print(movie_money)
    movie_aver_price = [movie.find_all("td")[3].string for movie in movies[1:]]
    print(movie_aver_price)
    movie_aver_person = [movie.find_all("td")[4].string for movie in movies[1:]]
    print(movie_aver_person)
    movie_country = [movie.find_all("td")[5].string for movie in movies[1:]]
    print(movie_country)
    movie_time = [movie.find_all("td")[6].string for movie in movies[1:]]
    print(movie_time)
    directors = [get_info(href) for href in movie_href]
    print(directors)
    # 利用pandas进行数据格式化
    df = pd.DataFrame({
        "movie_name": movie_name,
        "movie_href": movie_href,
        'movie_type': movie_type,
        "movie_money": movie_money,
        "movie_aver_price": movie_aver_price,
        "movie_aver_person": movie_aver_person,
        "movie_country": movie_country,
        "movie_time": movie_time,
        "directors": directors
    })
    print(df)
    # df.to_xxx()储存为xxx格式文件
    df.to_csv("movie_pandas_csv.csv")
    # pd.read_xxx 利用pandas进行读取xxx类型文件
    df_2 = pd.read_csv("movie_pandas_csv.csv")
    print(df_2.head())#head方法是读取前5行
def get_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36,h"
    }
    # print(666)
    rsp = requests.get(url, headers=headers)
    soup = BeautifulSoup(rsp.text, "lxml")
    # print(soup)
    # name = soup.select("dl[class='dltext'] a")[0].string
    name = soup.select("dl.dltext a")[0].string
    return name
if __name__ == "__main__":
    urls = ["http://www.cbooo.cn/year?year={}".format(str(i)) for i in range(2018, 2019)]
    for url in urls:
        movies_spider(url)