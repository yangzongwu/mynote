### 什么是wsgi？
WSGI是Python在处理HTTP请求时，规定的一种处理方式。如一个HTTP Request过来了，那么就有一个相应的处理函数来进行处理和返回结果。WSGI就是规定这个处理函数的参数长啥样的，它的返回结果是长啥样的？至于该处理函数的名子和处理逻辑是啥样的，那无所谓。简单而言，WSGI就是规定了处理函数的输入和输出格式。

### django请求的生命周期？
* 当用户在浏览器中输入url时,浏览器会生成请求头和请求体发给服务端
请求头和请求体中会包含浏览器的动作(action),这个动作通常为get或者post,体现在url之中.
* url经过Django中的wsgi,再经过Django的中间件,最后url到过路由映射表,在路由中一条一条进行匹配,
一旦其中一条匹配成功就执行对应的视图函数,后面的路由就不再继续匹配了.
* 视图函数根据客户端的请求查询相应的数据.返回给Django,然后Django把客户端想要的数据做为一个字符串返回给客户端.
* 客户端浏览器接收到返回的数据,经过渲染后显示给用户.

### 简述MVC和MTV
* MVC软件系统分为三个基本部分：模型(Model)、视图(View)和控制器(Controller)
    * Model：负责业务对象与数据库的映射(ORM)
    * View：负责与用户的交互
    * Control：接受用户的输入调用模型和视图完成用户的请求
* Django框架的MTV设计模式借鉴了MVC框架的思想,三部分为：Model、Template和View
    * Model(模型)：负责业务对象与数据库的对象(ORM)
    * Template(模版)：负责如何把页面展示给用户
    * View(视图)：负责业务逻辑，并在适当的时候调用Model和Template
* 此外,Django还有一个urls分发器,
    * 它将一个个URL的页面请求分发给不同的view处理,view再调用相应的Model和Template

### django路由系统中name的作用
用于反向解析路由,相当于给url取个别名，只要这个名字不变,即使对应的url改变,通过该名字也能找到该条url

### 列举django的内置组件？
* Admin是对model中对应的数据表进行增删改查提供的组件
* model组件：负责操作数据库
* form组件：1.生成HTML代码2.数据有效性校验3校验信息返回并展示
* ModelForm组件即用于数据库操作,也可用于用户请求的验证

### 列举django中间件的5个方法？以及django中间件的应用场景？
* process_request : 请求进来时,权限认证
* process_view : 路由匹配之后,能够得到视图函数
* process_exception : 异常时执行
* process_template_responseprocess : 模板渲染时执行
* process_response : 请求有响应时执行

### 简述什么是FBV和CBV？
FBV和CBV本质是一样的，基于函数的视图叫做FBV，基于类的视图叫做CBV  
在python中使用CBV的优点：
* 提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）
* 可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性

### django的request对象是在什么时候创建的？
```
class WSGIHandler(base.BaseHandler):
-------request = self.request_class(environ)
```
请求走到WSGIHandler类的时候，执行cell方法，将environ封装成了request

### cookie和session的区别：
* cookie:
cookie是保存在浏览器端的键值对,可以用来做用户认证
* session：
将用户的会话信息保存在服务端,key值是随机产生的字符串,value值是session的内容
依赖于cookie将每个用户的随机字符串保存到用户浏览器上  
Django中session默认保存在数据库中：django_session表  
flask,session默认将加密的数据写在用户的cookie中  

### django的Model中的ForeignKey字段中的on_delete参数有什么作用？
删除关联表中的数据时,当前表与其关联的field的操作  
django2.0之后，表与表之间关联的时候,必须要写on_delete参数,否则会报异常

### django中csrf的实现机制
* django第一次响应来自某个客户端的请求时,后端随机产生一个token值，把这个token保存在SESSION状态中;同时,后端把这个token放到cookie中交给前端页面；
* 下次前端需要发起请求（比如发帖）的时候把这个token值加入到请求数据或者头信息中,一起传给后端；Cookies:{csrftoken:xxxxx}
* 后端校验前端请求带过来的token和SESSION里的token是否一致。

### Django本身提供了runserver，为什么不能用来部署？(runserver与uWSGI的区别)
* runserver方法是调试 Django 时经常用到的运行方式，它使用Django自带的
WSGI Server 运行，主要在测试和开发中使用，并且 runserver 开启的方式也是单进程 。
* uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http 等协议。注意uwsgi是一种通信协议，而uWSGI是实现uwsgi协议和WSGI协议的 Web 服务器。uWSGI具有超快的性能、低内存占用和多app管理等优点，并且搭配着Nginx就是一个生产环境了，能够将用户访问请求与应用 app 隔离开，实现真正的部署 。相比来讲，支持的并发量更高，方便管理多进程，发挥多核的优势，提升性能。

### 什么是wsgi,uwsgi,uWSGI
* WSGI: web服务器网关接口,是一套协议。用于接收用户请求并将请求进行初次封装，然后将请求交给web框架
    实现wsgi协议的模块：
    * 1.wsgiref,本质上就是编写一个socket服务端，用于接收用户请求(django)
    * 2.werkzeug,本质上就是编写一个socket服务端，用于接收用户请求(flask)
* uwsgi:
    与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议,用于定义传输信息的类型
* uWSGI:
    是一个web服务器,实现了WSGI协议,uWSGI协议,http协议,
    
    
### 说一下Django，MIDDLEWARES中间件的作用和应用场景？
中间件是介于request与response处理之间的一道处理过程,用于在全局范围内改变Django的输入和输出。  
简单的来说中间件是帮助我们在视图函数执行之前和执行之后都可以做一些额外的操作  
例如：
* 1.Django项目中默认启用了csrf保护,每次请求时通过CSRF中间件检查请求中是否有正确#token值
* 2.当用户在页面上发送请求时，通过自定义的认证中间件，判断用户是否已经登陆，未登陆就去登陆。
* 3.当有用户请求过来时，判断用户是否在白名单或者在黑名单里

### Django中models利用ORM对Mysql 进行查表的语句
* all():返回模型类对应表格中的所有数据。
* get():返回表格中满足条件的一条数据，
* filter():参数写查询条件，返回满足条件 QuerySet 集合数据。

### 谈一下你对 uWSGI 和 nginx 的理解？
* uWSGI 是一个 Web 服务器，它实现了 WSGI 协议、uwsgi、http 等协议。Nginx 中HttpUwsgiModule 的作用是与 uWSGI 服务器进行交换。WSGI 是一种 Web 服务器网关接口。它是一个 Web 服务器（如 nginx，uWSGI 等服务器）与 web 应用（如用 Flask 框架写的程序）通信的一种规范。  
要注意 WSGI / uwsgi / uWSGI 这三个概念的区分。
    * WSGI 是一种通信协议。
    * uwsgi 是一种线路协议而不是通信协议，在此常用于在 uWSGI 服务器与其他网络服务器的数据通信。
    * uWSGI 是实现了 uwsgi 和 WSGI 两种协议的 Web 服务器。
* nginx 是一个开源的高性能的 HTTP 服务器和反向代理：
    * 1.作为 web 服务器，它处理静态文件和索引文件效果非常高；
    * 2.它的设计非常注重效率，最大支持 5 万个并发连接，但只占用很少的内存空间；
    * 3.稳定性高，配置简洁；
    * 4.强大的反向代理和负载均衡功能，平衡集群中各个服务器的负载压力应用。
    
    
### nginx 和 uWSGI 服务器之间如何配合工作的
首先浏览器发起 http 请求到 nginx 服务，Nginx 根据接收到请求包，进行 url 分析，判断访问的资源类型，如果是静态资源，直接读取静态资源返回给浏览，如果请求的是动态资源就转交给 uwsgi 服务器，uwsgi 服务器根据自身的 uwsgi 和 WSGI 协议，找到对应的 Django 框架，Django 框架下的应用进行逻辑处理后，将返回值发送到 uwsgi 服务器，然后 uwsgi 服务器再返回给 nginx，最后 nginx 将返回值返回给浏览器进行渲染显示给用户
![avtar](https://img-blog.csdnimg.cn/20190528140942518.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE4NjQ5MA==,size_16,color_FFFFFF,t_70)


### csrf 攻击原理
简单来说就是: 你访问了信任网站 A，然后 A 会用保存你的个人信息并返回给你的浏览器一个cookie，然后呢，在 cookie 的过期时间之内，你去访问了恶意网站 B，它给你返回一些恶意请求代码， 要求你去访问网站 A，而你的浏览器在收到这个恶意请求之后，在你不知情的情况下，会带上保存在本地浏览器的 cookie 信息去访问网站 A，然后网站 A 误以为是用户本身的操作，导致来自恶意网站 C 的攻击代码会被执：发邮件，发消息，修改你的密码，购物，转账，偷窥你的个人信息，导致私人信息泄漏和账户财产安全收到威胁

### ngnix 的正向代理与反向代理
web 开发中，部署方式大致类似。简单来说，使用 Nginx 主要是为了实现分流、转发、负载均衡， 以及分担服务器的压力。Nginx  部署简单，内存消耗少，成本低。Nginx  既可以做正向代理，也可以做反向代理。
* 正向代理：请求经过代理服务器从局域网发出，然后到达互联网上的服务器。特点：服务端并不知道真正的客户端是谁。
* 反向代理：请求从互联网发出，先进入代理服务器，再转发给局域网内的服务器。特点：客户端并不知道真正的服务端是谁。
* 区别：正向代理的对象是客户端。反向代理的对象是服务端。


### 请简述浏览器是如何获取一枚网页的
* 在用户输入目的 URL 后，浏览器先向 DNS 服务器发起域名解析请求；
* 在获取了对应的 IP 后向服务器发送请求数据包；
* 服务器接收到请求数据后查询服务器上对应的页面，并将找到的页面代码回复给客户端；
* 客户端接收到页面源代码后，检查页面代码中引用的其他资源，并再次向服务器请求该资源；
* 在资源接收完成后，客户端浏览器按照页面代码将页面渲染输出显示在显示器上；

###  Django对数据查询结果排序怎么做，降序怎么做，查询大于某个字段怎么做
* 排序使用 order_by()
* 降序需要在排序字段名前加-



### Django 重定向你是如何实现的？用的什么状态码
* 使用 HttpResponseRedirect
* redirect 和 reverse
* 状态码：302,301

###  关系型数据库的关系包括哪些类型
* ForeignKey：一对多，将字段定义在多的一端中。
* ManyToManyField：多对多：将字段定义在两端中。
* OneToOneField：一对一，将字段定义在任意一端中