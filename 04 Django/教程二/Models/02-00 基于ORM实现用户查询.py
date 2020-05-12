'''
urls.py
urlpatterns=[
    path('admin/', admin.site.urls),
    url(r'^cmdb/',include('app01.url')),
    #url(r'^monitor/',include('app02.url'))
]
'''

'''
1: urls.py
urlpatterns = [url(r'^index/',views.index,name='indexx'),]

2: views.py
def index(request):
    return render(request,'index.html')

3: index.html
<div>
        <a class="menu" href="/cmdb/user_info/">用户管理</a>
        <a class="menu" href="/cmdb/user_group/">用户组管理</a>
 </div>
 
4. urls.py
urlpatterns = [url(r'^user_info/',views.user_info),]

5: views.py
def user_info(request):
    user_list=models.UserInfo.objects.all()
    #print(user_list.query)# 查看当前SQL语句
    return render(request, 'user_info.html',{'user_list':user_list})
 
6:user_info.html
<div>
        <h3>用户列表</h3>
        <ul>
            {% for row in user_list %}
                <li> <a href="/cmdb/userdetail-{{ row.id }}/">{{ row.username }}</a></li>
            {% endfor %}
        </ul>
    </div>

7: urls.py
urlpatterns = [url(r'^userdetail-(?P<nid>\d+)/',views.user_detail),]


8: views.py
def user_detail(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    #models.UserInfo.objects.get(id=nid)  可以取单条数据，但是容易报错需要try一下
    return render(request,'user_detail.html',{'obj':obj})

9:user_detail.html
    <div>
        <h1>用户详细信息</h1>
        <h5>{{ obj.id }}</h5>
        <h5>{{ obj.name }}</h5>
        <h5>{{ obj.password }}</h5>
    </div>
'''
