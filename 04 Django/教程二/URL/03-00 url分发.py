from django.contrib import admin
from django.urls import path
from app01 import views
from django.conf.urls import url,include


'''
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/',views.index,name='indexx'),
    url(r'^login/',views.login),
    url(r'^home/',views.Home.as_view()),
    #url(r'^detail/',views.detail),
    url(r'^detail-(\d+).html/',views.detail),
]
'''

#  URL 通过include分发
#  案例分工》如何处理？

urlpatterns=[
    path('admin/', admin.site.urls),
    url(r'^cmdb/',include('app01.url')),
    url(r'^monitor/',include('app02.url'))
]
