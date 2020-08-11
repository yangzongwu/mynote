import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, 'html.parser')
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    # .get_text() 所有的标签都清除，返回只包含文字的字符串
    print(name.get_text())


"""
findAll(tag , attrs , recursive , text , limit, **kwargs)
find(tag , attrs , recursive , text , **kwargs)
eg:
.findAll({"h1","h2","h3","h4","h5","h6"})
.findAll("span", {"class": "green"})
recursive: 默认True，查看子孙标签，设为False只查一级标签
text:是用标签的文本内容去匹配，而不是标签的属性
nameList = bsObj.findAll(text="the prince")
limit:标签的前几项
kwargs：eg id="text"
"""


"""
正则表达式
如下查找所有以 ../img/gift/img 开头，以.jpg结尾的图片
"""
image = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gift\/img.*\.jpg")})


"""
Lambda 表达式
"""
bsObj.findAll(lambda tag: len(tag.attrs)==2)
