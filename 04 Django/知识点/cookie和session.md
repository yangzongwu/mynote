# 简介
### HTTP无状态性  
* HTTP协议不具备保存之前发送过的请求或响应的功能，每一次请求都被协议认为是一次性的
* HTTP引入了session和cookie（session和cookie都是缓存），既保持了http的
无状态性，也使得http的应用称为有状态的

### session和cookie
###### cookies
* cookies是指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）。
cookie大致上分为两种，分别是会话cookie和持久化cookie。
    * 会话cookie是存放在客户端浏览器的内存中，他的生命周期和浏览器是一致的，当浏览器关闭会话cookie也就消失了，
    * 持久化cookie是存放在客户端硬盘中，持久化cookie的生命周期是我们在设置cookie时候设置的那个保存时间。
###### session
* session是存储在服务端的，获取方式：通过cookie里的session id（通过服务器
生成）获取，而session是存放在服务器的内存中的，所以session的数据不断增加会
造成服务器的负担，所以只会把很重要的信息存储在session中，而把一些次要的东西
存储在客户端的cookie中
###### session id
* 当客户端第一次请求session时，服务器端会为客户端创建一个session对象，并且生
成一个session id(通过一些加密算法)。然后保存在cookie中。当用户再次登录时，
客户端通过cookie，将session id传到服务器，去和服务器中的session id进行对
比，寻找这个session 。然后根据查找结果执行对应的操作
######  id被盗可能导致的问题                                                                                      
因为session Id是保存在cookie中，而cookie是存在于客户端，所以session 
Id 并不安全
######  如何避免
* 敏感操作需要用户输入密码来进行二次认证
* 网站https化，提高消息传递过程中的安全系数
* 用户使用一个密匙对参数进行hash，这样即使cookie被盗取，也会因为没有密匙
而无法获取session id

# Cookie
第一次请求，post提交自己的用户名及密码，然后服务端给它回一个带有cookie的消息，
客户端以后再向服务器发送任何请求消息时都会携带cookie，服务端只需要验证cookie
就可以判断是否客户端是否之前登陆成功过！
* send: cookie:{}
* receive: set_cookie:user=xxx,is_login=True
* second send: cookie:{user:xxx,is_login:True}
### 特点
* Cookie以键值对的格式进行信息的存储;
* Cookie基于域名安全,不同域名的Cookie是不能互相访问的,
    * 如访问google.com,同一浏览器访问baidu.com时,无法访问到google.com写到Cookie信息.
* 当浏览器请求某网站时,会将浏览器存储的跟网站相关的所有Cookie信息提交给网站服务器.
* cookie是有过期时间的，如果不指定时间，默认会关闭浏览器则失效
### 优点:
* 解决了 HTTP协议的“无状态”模式。
* 数据存储在客户端（端存储）。减轻服务端的压力，提高网站的性能
### 缺点:
* 安全性较差；
* 存储量小,最大支持4096字节。需要靠 Session 来弥补。
### cookie的使用接口
django的服务端发送响应有三种方式：
```python
    return HttpResponse()
    return render()
    return redirect()
```
### Django中操作Cookie
* 设置Cookies
```python
response = redirect("/index/")或 HttpResponse(...) 或  render(request, ...) 

# 第一种方法（推荐）
response.set_cookie("islogin",True)  # 设置cookie值，注意这里的参数，一个是键，一个是值
response.set_cookie("lilz","344",20)  # 20单位为秒，代表max_age：过期时间
response.set_cookie("username", username)
	
# 第二种方法
response.set_cookie(key,value,...)

# 第三种方法
response.set_signed_cookie(key,value,salt='加密盐',...)
```
* 获取Cookies
```python
# 如果当前请求的cookie中存在username并且有值，那么就获取，没有就用这里给的默认值None
username=request.COOKIES.get("username",None)
```
* 删除Cookies
```python
response.delete_cookie("username",path="/",domain=name)
```
* 检测Cookies
```python
if "username" in request.COOKIES :
    xxx
```
### 案列
```python

# Add Cookie.
def add_cart(request):
    # 购物车是在COOKIE good_id,count
    goods_id = request.GET.get('id', '')
    if goods_id:
        # 获取上一个页面的地址
        prev_url = request.META['HTTP_REFERER']
        response = redirect(prev_url)
        goods_count = request.COOKIES.get(goods_id)
        if goods_count:
            goods_count = int(goods_count) + 1
        else:
            goods_count = 1
        response.set_cookie(goods_id, goods_count)
    return response

# Search Cookie
def show_cart(request):
    cart_goods_list=[]
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.num = goods_num
        cart_goods_list.append(cart_goods)
    return render(request, "cart/cart.html", {'cart_goods_list': cart_goods_list,})

# remove Cookie
def submit_order(request):
    response = redirect('/cart/submit_success/?id=%s' % order_info.order_id)
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        response.delete_cookie(goods_id)
    return response
```
# Session
![avatar](https://img-blog.csdnimg.cn/20200729235633542.png?)
* 首先浏览器第一次发送post提交user，pwd的请求，携带的是一个空的cookie访问服务器；(cookie:{})
* 然后服务器往session里写入键值（如request.session[“username”]=“y”）时，找到django-session表，
生成随机字符串当作键放在session-key中，把写的键值放入session-data中；
(session['123432sdfs']={"username":"y"})
* 然后服务器给客户端响应，把随机生成的字符串设置给cookie然后返回响应；(set_cookie:sessionid='123432sdfs')
* 客户端以后再访问服务器就会携带cookie。而服务器就会根据cookie里面的sessionid值与django-data表里的sessionkey匹配。
若匹配上则表示客户端登陆成功过.(cookie:{sessionid:'123432sdfs'})

### Django启动Session
Django项目默认启用session，在setting.py文件中
```python
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    ......
]
```
### 存储方式
在settings.py文件中，可以设置session数据的存储方式;  
另外session可以保存在数据库、本地缓存( 程序的运行内存中, 全局变量)、文件、redis等   
* 数据库  
存储在数据库中,如下设置可以写,也可以不写,这是默认存储方式
```python
SESSION_ENGINE='django.contrib.sessions.backends.db'
INSTALLED_APPS = [
    'django.contrib.sessions',
    '......'
]
```
* 本地缓存  
```python
SESSION_ENGINE='django.contrib.sessions.backends.cache'
```
* redis
```
pip install django-redis
```
```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 定义django中redis的位置
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            # django使用redis的默认客户端来进行操作.
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# 我们定义一个cache(本地缓存来存储信息,cahe指定的是redis)
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 本地的session使用的本地缓存名称是'default', 这个名称就是上面我们配置的caches的名
# 称"default"
SESSION_CACHE_ALIAS = "default"
```
### session操作
```python
# 以键值对的格式写session
request.session['one'] = '1'
# 根据键读取值
one = request.session.get('one')
# 清除所有session，在存储中删除值部分.
request.session.clear()
# 清除session数据，在存储中删除session的整条数据。
request.session.flush()
# 删除session中的指定键及值，在存储中只删除某个键及对应的值。
del request.session['键']
# 设置session的有效期
request.session.set_expiry(value)
```