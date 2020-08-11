# 爬虫与验证码
* 验证码：门户网站的反爬机制，识别验证码图片中的数据，用于模拟登录
* 识别方法：
    * 人工肉眼识别（不推荐）
    * 第三方自动识别（http://fast.95man.com/auth/quickchk.html）
* 识别步骤：        
    * 下载验证码图片
    * 利用第三方提供的API接口class类，调用得到验证码
    * 模拟登录
    * 登录失败再次循环验证

# Http/Https 协议特征
无状态协议，发起的第二次基于个人主页页面请求的时候，服务器端
不知道此请求是基于登录状态下的请求，
* 第一次模拟登录，
* 第二次发起个人主页数据（服务器不知道是否登录）

# cookie
用来让服务器端记录客户端相关状态
* 手动处理(不推荐)
* 自动处理
    * cookie 来源与模拟登录post请求后，由服务器端创建
    * session 可以进行请求的发送，如果请求过程中产生了cookie，该cookie会被自动存储在该session对象中
* 步骤
    * 创建一个session对象，session=request.Session()
    * 使用session对象进行模拟登录post请求的发送
    * session 对象对个人主页对应的get请求进行发送(携带了cookie)
    
 
# 人人网模拟登录
```python
import os
from lxml import etree
import requests

def login():
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

    def PostPic(filepath, codetype):
        """
        imbyte: 图片字节
        imgtype: 类型 1为通用类型 更多精准类型请参考 http://fast.net885.com/auth/main.html
        """
        strRtn = ''
        imbyte = open(filepath, 'rb').read()
        filename = os.path.basename(filepath)

        files = {'imgfile': (filename, imbyte)}
        r = requests.post(
            'http://api.95man.com:8888/api/Http/Recog?Taken=' + 'jtieWeoEN49wBnBnXnymcTF1Lwkz' + '&imgtype=' + str(
                codetype) + '&len=0',
            files=files, headers=headers)
        print(r.text)
        arrstr = r.text.split('|')
        # 返回格式：识别ID|识别结果|用户余额
        if (int(arrstr[0]) > 0):
            strRtn = arrstr[1]
        return strRtn


    while True:
        url = 'http://www.renren.com/syshome.do'
        page_text=requests.get(url=url,headers=headers).text
        tree=etree.HTML(page_text)
        code_img_src=tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
        code_img_data=requests.get(url=code_img_src,headers=headers).content
        with open('./code.jpg','wb') as fp:
            fp.write(code_img_data)
        result=PostPic('code.jpg',1)
        print(result)
        login_url='http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2020642348380'
        data={
            'email': 'yangzong5@163.com',
            'password': 'yzw4725255',
            'icode': '',
            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id':'1',
            'captcha_type': 'web_login',
            'f':'',
        }
        # 使用session进行POST请求的发送
        response=session.post(url=login_url,headers=headers,data=data)
        try:
            login_page_json=response.json()
            print(login_page_json)
        except:
            login_page_text=response.text
            with open('renren.html','w',encoding='utf-8') as fp:
                fp.write(login_page_text)
                print('login')
            break

    detail_url='http://www.renren.com/737907985/profile'
    #使用session进行get请求的发送
    detail_page_text=session.get(url=detail_url,headers=headers).text
    with open('detail.html','w',encoding='utf-8') as fp:
        fp.write(detail_page_text)
login()
```

# 代理
如果一个IP频繁访问服务器，服务器可能会拒绝该IP,代理就是破解封IP这种防爬机制
* 什么是代理：代理服务器
* 代理的作用：突破自身IP访问的限制，可以隐藏自身真实IP
* 代理相关网站：
    * 快代理
    * 西祠代理
    * www.goubanjia.com