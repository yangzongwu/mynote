#new include function
#first_project
#  urls.py
    from django.conf.urls import include
    urlpatterns = [
      url(r'^first_app/',include('first_app.urls')),
    ]
 
#Then under first_app folder new file: urls.py
  from django.conf.urls import url
  from first_app import views
  urlpatterns=[
    url(r'^$',views.index,name='index'),
  ]

   
   
