from urllib.request import urlretrieve,urlopen
from bs4 import BeautifulSoup

def saveSingleFile():
    """
    这段程序从http://XXX 下载图片，
    然后在程序运行的文件夹里保存为logo.jpg 文件
    """
    html = urlopen("https://tieba.baidu.com/p/6674193657")
    bsObj = BeautifulSoup(html, "html.parser")
    imageLocation = bsObj.find('div', {"id": "post_content_132104804021"}).find("img")["src"]
    urlretrieve(imageLocation, "logo.jpg")

# 如果需要批量下载图片？