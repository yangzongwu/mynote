#first project
'''
change dir
In Atom : file-- add project folder
activate myDjangoEnv
django -admin startproject first_project
'''
#under project:
first_project #项目的容器。
    __init__.py #一个空文件，告诉 Python 该目录是一个 Python 包。
    settings.py #该 Django 项目的设置/配置。
    urls.py #该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
    wsgi.py #一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
  manage.py #一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互
  
python manage.py runserver

'''
A Django Project is a collection of appications and configurations that when conbined 
together will make the full web appliction
under project:
python manage.py startapp first_app
'''

fist_app
  migrations # 数据库每次改动都会在这个目录下生成一条记录 
  __init__py # 说明这是个python包
  admin.py # 管理后台的文件
  apps.py
  models.py # models文件，主要编写一些数据库的表结构，字段等
  test.py # 测试用的文件
  view.py # 试图函数的文件，大多数我们是在这个文件进行页面逻辑的编写
  templates  # 这个目录是自己建立的，里面放我的html的模板页面
  static   # 这个目录是自己简历的，里面放我的静态文件，比如.css .js 
  
 
#a simple example: 
step1:
    first_project
        setting.py
        INSTALLED_APPS = [
            'first_app' #add this
            ]
step2:
    first_app
        view.py
        from django.http import HttpResponse
        def index(request):
            return HttpResponse("Hello World!")
step3:
    #map view to urls.py
    first_project
        urls.py
        from django.conf.urls import url
        from first_app import views
            urlpatterns = [
            url(r'^$',views.index,name='index'),
        ]
python manage.py runserver
