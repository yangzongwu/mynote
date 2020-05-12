#  1.创建Django工程  
django-admin startproject [工程名字]  

mysite  
* mysite    # 对整个程序进行配置
    * init  
    * setting  #配置文件
    * url      #URL对应关系  
    * wsgi     #遵循WSGI规范，一般用uwgi+nginx
* manage.py   #管理Django程序  
>python manage.py  
>python manage.py startapp xx  
>python manage.py makemigrations  
>python manage.py migrate
### 运行Django功能  
python manage.py runserver 127.0.0.1:8001

#  2.创建APP  
cd 工程名
python manage.py startapp xx 一般来说创建多个独立APP
* myapp  
    * migrations # 数据库操作记录，修改表结构
    * init # python2必须有，python3 可以不需要
    * admin #Django 默认创建的后台管理
    * apps  #对当前APP配置
    * models #ORM,写制定的类，通过命令创建创建数据库
    * tests #单元测试
    * views #业务代码

#  3.配置模板路径templates  
TEMPLATES = [{  
        'DIRS': [os.path.join(BASE_DIR,'templates')],  
     }]
#  4.配置静态目录static  
STATIC_URL = '/static/'  
STATICFILES_DIRS=[  
    os.path.join(BASE_DIR,'static'),  
]  

#  5.setting中
  middlerware
  注释掉 csrf
 
#  6.定义路由规程URLS
urls.py  
"login"-->函数

#  7.定义试图函数  
app/views.py
def func(request):  
>request.method GET/POST  
>requst.GET.get('',None)# 获取请求发来的数据  
>requst.POST.get('',None)  

>return HttpResponse("字符串")  
>return render(request,"HTML模板的路径")  
>return redirect("HTML模板的路径") 不允许  
>return redirect("只能填URL")  

#  8.模板渲染  
特殊的模板语言  
