url.py
from app01 import views
from django.conf.urls import url
urlpatterns = [
    url(r'^login/',views.login),
]

view.py
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
# Create your views here.
def home(requst):
    return  HttpResponse('<h1>Hello<h1>')
def login(request):
    '''
      f=open('templates/login.html','r',encoding='utf-8')
        data=f.read()
        f.close()
        return  HttpResponse(data)
    '''
      #return render(request,'login.html')#等同于上面
    
    #request 包含了用户提交的所有信息
    #print(request.method)
    #GET OR POST
    
    # 获取用户提交方法
    error_msg=''
    if request.method=='POST':
        #获取用户通过POST提交过来的数据
        user=request.POST.get('user',None)
        pwd=request.POST.get('pwd',None)

        if user=='root' and pwd=='123':
            #跳转到相关页面
            return redirect('https://www.baidu.com')
        else:
            #用户名密码不匹配
            error_msg='用户名密码不匹配'
    return render(request, 'login.html',{'error_msg':error_msg})


templates/login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/commons.css">
</head>
<body>
    <form action="/login" method="post">
        {% csrf_token %}
        <p>
            <label for="username">username：</label>
            <input id="username" name='user' type="text"/>
        </p>
        <p>
            <label for="password">password：</label>
            <input id='password' name='pwd' type="text"/>
            <input type="submit" value="submit">
            <span style="color: red;">{{ error_msg }}</span>
        </p>
    </form>
</body>
</html>
