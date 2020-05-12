from django.contrib import admin
from django.urls import path
from app01 import views
from django.conf.urls import url,include


#-------------01--------------------------------------------------

urlpatterns = [
    url(r'^detail-(\d+).html/',views.detail),  
]
def detail(request,nid):
    detail_info=USER_DICT[nid]


#-------------02--------------------------------------------------

urlpatterns = [
    url(r'^detail-(\d+)-(\d+).html/',views.detail),#可以有多个ID  
]    
def detail(request,nid,uid):#默认情况下严格安装顺序存储的，动态路由关系
    detail_info=USER_DICT[nid]


#-------------03--------------------------------------------------

#正则表达式分组格式
urlpatterns = [
    url(r'^detail-(?P<nid>\d+)-(?P<nid>\d+).html/',views.detail),#可以有多个ID  
] 
def detail(request,nid=1,uid=3):#nid uid 不用顺序，指定哪个形参是多少
    detail_info=USER_DICT[nid]
    
    
#-------------参数传递-------------------------------------------------- 

#参数是顺序过来的，存储在argsl里面，元组
urlpatterns = [
    url(r'^detail-(\d+)-(\d+).html/',views.detail),#可以有多个ID  
]  
def detail(request,*args,**kwargs):
    pass
    
    
#如下模式，存在kwargs里面，字典    
urlpatterns = [
    url(r'^detail-(?P<nid>\d+)-(?P<nid>\d+).html/',views.detail),#可以有多个ID  
] 
def detail(request,*args,**kwargs):
    pass
    
