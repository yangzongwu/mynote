urlpatterns = [
    #url(r'^index/',views.index),
    
    #当前访问的URL：index，每次修改的时候需要修改url.py.同时还需要改html
    #django 特有 name='indexx'
    url(r'^index/',views.index,name='indexx'),
    #<form action={% url 'index' %} method="POST">
    
    #只传了一个indexx，前缀，后面的值拿不到会报错，需要修改form如下
    #如下2只是帮你生成URL方式
    url(r'^index/(\d+)/',views.index,name='indexx'),
    #<form action={% url 'index' 2 %} method="POST">
    
    #如果需要生成当前的URL？
    #修改form,
    <form action={{ request.path.info }} method="POST">
]

#name:
#  对URL路由关系进行命名，以后可以根据此名称生成自己想要的URL
#  url(r'^index/',views.index,name='indexx'),
#  模板语言 {% url 'indexx' %}
#  url(r'^detail/?(\d+).html/',views.detail),
#  模板语言 {% url 'indexx' 3 %}
#  当前的URL
#  模板语言 {{ request.path.info }}



#view.py
#reverse反转，根据名字反转生成URL

url(r'^index/',views.index,name='indexx'),
def index(request):
    from django.urls import reverse
    v=reverse('indexx')
#/index/

url(r'^index/(\d+)/',views.index,name='indexx'),
def index(request):
    from django.urls import reverse
    v=reverse('indexx',args=(90,)) 生成新的URL
    return render(request, 'index.html', {'user_dict':USER_DICT})
#/index/90/

url(r'^detail-(?P<nid>\d+)-(?P<nid>\d+).html/',views.index,name='indexx'),
def index(request,nid,uid):
    from django.urls import reverse
    v=reverse('indexx',kwargs=('nid':90,'uid':10)) 生成新的URL
    return render(request, 'index.html', {'user_dict':USER_DICT})
#/index/90/10

#form也需要同时变更传递参数




#三种形式
#    url(r'^index/',views.index,name='i1'),
#    url(r'^detail/(\d+)/(\d+)/',views.detail,name='i2'),
#    url(r'^detail/?P<nid>(\d+)/?P<uid>(\d+)/',views.detail,name='i3'),
#
# view.py
#  reverse 自动生成URL
#  def func(request.*args,**kwargs):
#      from django.urls import reverse
#      url1=reverse('i1') #index/
#      url2=reverse('i2',args=(1,2,)) #index/1/2
#      url3=reverse('i3',kwargs={'nid':1,'uid':2}) #index/1/2
#
#  xxx.html 自动生成URL
#  {% url 'i1' %}     #index/
#  {% url 'i2' 1 2 %} #index/1/2
#  {% url 'i3' nid=1 nid=2 %} #index/1/2
