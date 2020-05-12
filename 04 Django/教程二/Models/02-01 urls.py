from django.contrib import admin
from django.urls import path
from app01 import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'^index/',views.index,name='indexx'),
    url(r'^login/',views.login),
    url(r'^orm/',views.orm),
    url(r'^user_info/',views.user_info),
    url(r'^userdetail-(?P<nid>\d+)/',views.user_detail),
]
