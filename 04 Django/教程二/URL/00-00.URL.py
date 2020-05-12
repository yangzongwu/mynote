from django.contrib import admin
from django.urls import path
from app01 import views
from django.conf.urls import url,include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/',views.index,name='indexx'),
    url(r'^detail/',views.detail),
    #---02---
    url(r'^detail-(\d+).html/',views.detail),
]
