from django.conf.urls import url
from AppTwo import views
urlpatterns=[
    #url(r'^$',views.help,name='index'),
    url(r'^$',views.user,name='user'),
]
