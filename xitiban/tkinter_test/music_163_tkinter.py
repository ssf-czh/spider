'''
爬取网易云音乐
并且做成图形化界面

网易云有个外部下载链接http://music.163.com/song/media/outer/url?id={}.mp3   .format()
每一首个都有一个特定的id 需要自己去爬取某个歌单里的歌的id
注意 ：浏览器看到的歌单链接并不是真实的链接 需要自己通过preview进行抓包 而且放回的源码和浏览器看到的源码是不一样的
比如  https://music.163.com/#/playlist?id=2645113725 通过抓包得到真实url：https://music.163.com/playlist?id=2645113725
观察到少了 #/
所以在人机界面交互的时候 可以优化(实际上请求的网页还是没有#/的网页)
'''

from tkinter import *
import requests
from bs4 import BeautifulSoup
from urllib import request
from lxml import etree

def music_spider():
    headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.3"
    }
    url = entry.get()
    url = url.split("#/")
    url = "".join(url)
    print(url)
    rsp = requests.get(url=url, headers=headers)
    # print(rsp.text)
    # html = BeautifulSoup(rsp.text, "lxml")
    #
    # items = html.find_all("span", class_='txt')
    # print(items)

    html = etree.HTML(rsp.text)

    song_ids = html.xpath("//ul[@class='f-hide']//li/a/@href")
    song_names = html.xpath("//ul[@class='f-hide']//li/a/text()")
    # print(song_ids)
    # print(song_ids,song_names)
    path = r"G:\Git_Repository\spider\习题班\tkinter_test\music_163"
    for song_id, song_name in zip(song_ids, song_names):
        rsp = requests.get("http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id.strip("/song?id=")), headers=headers)
        print("http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id.strip("/song?id=")))
        # 添加数据到控件中 跟新
        text.insert(END, "正在下载{}".format(song_name))
        text.see(END)
        text.update()

        print(rsp.status_code)
        # request.urlretrieve(url="http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id.strip("/song?id=")),filename=path + '\\' + song_name + '.mp3')
        with open(path + '\\' + song_name + '.mp3',"wb") as f:
            f.write(rsp.content)








# 创建一个窗口
root =Tk()

# 设置窗口的标题
root.title("网易云音乐下载器")

# 设置窗口的大小
root.geometry("900x500")

# 设置窗口出现的位置
root.geometry("+400+150")

# 设置标签
lable = Label(root, text="输入你要下载的音乐:", font=("隶书", 22)) #仅仅是设置了标签 并没有在窗口上显示出来

lable.grid() # 定位 自动分为2*2    让标签分格  显示出来

#设置输入框
entry = Entry(root, font=("隶书", 20))

entry.grid(row=0, column=1) #定位 由于table将窗口分格成2*2 所以可以放在第0行第一列

# 设置列表框
text = Listbox(root, font=("隶书", 20), width=65, height=13)

text.grid(row=1, columnspan=2)#columnspan 横跨2列

# 设置按钮
button = Button(root, text='Start', font=("隶书", 20), comman=music_spider)

button.grid(row=2, column=0)

exit = Button(root, text='exit', font=("隶书", 20), comman=root.quit)#comman 后面跟的是函数名

exit.grid(row=2, column=1)

# 窗口的显示
root.mainloop()



