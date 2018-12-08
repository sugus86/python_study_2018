import requests
import re
import tkinter
 
#获取gethush
def gethush(music):
    global musicname
    musicname = music
    url = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery1910026785707623246724_1490845878865&keyword={}&page=1&pagesize=30&userid=-1&%20%20clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1490845878887'.format(musicname)
    response = requests.get(url)
    html = response.text
    pattern = '"FileHash":"(.*?)","SQPayType".*?"AlbumID":"(.*?)"'
    hush = re.search(pattern,html).group(1)
    album = re.search(pattern,html).group(2)
    return hush
 
#获取音乐下载链接
def getmusicurl(hush):
    url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}'.format(hush)
    response = requests.get(url)
    html = response.text
    pattern = '"play_url":"(.*?)","authors"'
    music_url = re.search(pattern,html).group(1)
    return music_url
 
#下载音乐
def downloadmusic(url):
    session = requests.Session()
    url = url.replace('\\','')
    r = requests.get(url)
    with open(r'd:\mp3\%s.mp3' % musicname, "wb") as f:
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                print('正在下载:%s'% musicname)
                f.write(chunk)
 
if __name__ == '__main__':
    ytm = tkinter.Tk()  # 创建Tk对象
    ytm.title("音乐下载器1.0")  # 设置窗口标题
    ytm.geometry("300x100")  # 设置窗口尺寸
    l1 = tkinter.Label(ytm, text="歌曲：")  # 标签
    l1.pack()  # 指定包管理器放置组件
    musicname = tkinter.Entry()  # 创建文本框
    musicname.pack()
 
 
    def down():
        print(musicname)
        user = musicname.get()  # 获取文本框内容
        hush = gethush(user)
        url = getmusicurl(hush)
        downloadmusic(url)
 
 
    tkinter.Button(ytm, text="下载", command=down).pack()  # command绑定获取文本框内容方法
    ytm.mainloop()
