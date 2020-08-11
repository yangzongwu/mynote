from urllib.request import urlopen
from requests import HTTPError
from bs4 import BeautifulSoup

"""
初识爬虫
注意抛出异常
"""


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title is None:
    print("title could not be found")
else:
    print(title)
