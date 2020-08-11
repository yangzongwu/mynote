# 基本知识
TCP/IP简介
https://www.liaoxuefeng.com/wiki/1016959663602400/1017787663253120  
HTTP协议简介
https://www.liaoxuefeng.com/wiki/1016959663602400/1017804782304672  

# requests
requests 库的安装    
http://docs.python-requests.org/zh_CN/latest/user/quickstart.html  
http://docs.python-requests.org/en/master/api/  
```
pip install requests
```

### get 
```
import requests
r=requests.get("https://tieba.baidu.com/p/6772875387")
print(type(r)) # <class 'requests.models.Response'>
#print(r.text)
```
```
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("https://tieba.baidu.com/p/6772875387", params=payload)
```
### POST
```
r = requests.post("https://tieba.baidu.com/p/6772875387")
```
```
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://tieba.baidu.com/p/6772875387", data=payload)
```

# beautifulsoup
### 初识
```
pip install beautifulsoup4
```
HTML原文档
```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify()) 按照标准的缩进格式的结构输出
print(soup.title)  # <title>The Dormouse's story</title>
print(soup.title.name)  # title
print(soup.title.string)  # The Dormouse's story
print(soup.title.parent.name)  # head
print(soup.p)  # <p class="title"><b>The Dormouse's story</b></p>
print(soup.p['class'])  # ['title']
print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.find_all('a'))  # [<a>...</a>,<a>...</a>,<a>...</a>]
print(soup.find(id="link3"))  # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# 打印所有<a>链接
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text()) # 获取温度所有文字内容
```
### 文档解析器
* BeautifulSoup(markup,"html.parser")
* BeautifulSoup(markup,"lxml")
* BeautifulSoup(markup,["lxml-xml"])
* BeautifulSoup(markup,"xml")
* BeautifulSoup(markup,"html5lib")

### 对象 tag
* 名字
```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
tag.name  # b
tag.name = "blockquote" # 更改名字
tag  #  <blockquote class="boldest">Extremely bold</blockquote>
```
* 属性
```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
tag['class']  # boldest
tag['class'] = 'verybold' # <blockquote class="verybold">Extremely bold</blockquote>
tag['id'] = 1 # <blockquote class="verybold" id="1">Extremely bold</blockquote>
del tag['class']
del tag['id'] # # <blockquote>Extremely bold</blockquote>
tag['class']  # KeyError : 'class'
print(tag.get('class'))  # None
```
* 多值属性
    * 在Beautiful Soup中多值属性的返回类型是list
    * 如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回
 
### 字符串
    * 字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串  
    * tag中包含的字符串不能编辑,但是可以被替换成其它的字符串
```python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
tag.string  # 'Extremely bold'
type(tag.string)  # <class 'bs4.element.NavigableString'>
tag.string.replace_with("No longer bold")
tag  # <b class="boldest">No longer bold</b>
```

### BeautifulSoup
```python
soup.name  # u'[document]'
```

### 注释
```python
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string  # "Hey, buddy. Want to buy a used parser"
type(comment)
# <class 'bs4.element.Comment'>
```


# 遍历文档树
```python
html_doc = """<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
```
### 子节点，父节点
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
# tag的 .contents 属性可以将tag的子节点以列表的方式输出:
head_tag = soup.head # <head><title>The Dormouse's story</title></head>
print(head_tag.contents)  # [<title>The Dormouse's story</title>]
title_tag = head_tag.contents[0]  # <title>The Dormouse's story</title>
print(title_tag.contents)  #["The Dormouse's story"]
# BeautifulSoup 对象本身一定会包含子节点,也就是说<html>标签也是 BeautifulSoup 对象的子节点
print(len(soup.contents))  # 1
print(soup.contents[0].name)  # html
for child in title_tag.children:
    print(child)                 # The Dormouse's story
#.descendants 所有子孙节点

title_tag = soup.title
title_tag  # <title>The Dormouse's story</title>
title_tag.parent  # <head><title>The Dormouse's story</title></head>
# .parents是所有父辈节点
```

### 兄弟节点
```python
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
sibling_soup.b.next_sibling  # <c>text2</c>
sibling_soup.c.previous_sibling  # <b>text1</b>
```

#  搜索文档树
```
find_all( name , attrs , recursive , string , **kwargs )
```
* name 参数：可以查找所有名字为 name 的tag。
* attr 参数：就是tag里的属性。
* string 参数：搜索文档中字符串的内容。
* recursive 参数： 调用tag的 find_all() 方法时，Beautiful Soup会检索当前tag的所有子孙节点。
如果只想搜索tag的直接子节点，可以使用参数 recursive=False

```python
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all("a", limit=2)
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
soup.find(string=re.compile("sisters"))
# u'Once upon a time there were three little sisters; and their names were\n'
```

# 第一个简单的爬虫案列
```python
import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
import os  #导入os模块

class BeautifulPicture():

    def __init__(self):  #类的初始化操作
        self.web_url = 'https://tieba.baidu.com/p/6761497345?pid=132933799920&cid=0#132933799920'
        self.folder_path = '/BeautifulPicture'

    def get_pic(self):
        r = requests.get(self.web_url)
        all_img = BeautifulSoup(r.text, 'html.parser').find_all('img', class_='BDE_Image')
        self.mkdir(self.folder_path)  #创建文件夹
        os.chdir(self.folder_path)   #切换路径至上面创建的文件夹
        
        cnt=1
        for a in all_img:
            img_str = a['src']
            self.save_img(img_str, str(cnt))
            cnt+=1

    def save_img(self, url, name): ##保存图片
        img = requests.get(url)
        file_name = name + '.jpg'
        with open(file_name, 'wb') as fp:
            fp.write(img.content)

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        else:
            pass

beauty = BeautifulPicture()  #创建类的实例
beauty.get_pic()  #执行类中的方法
```