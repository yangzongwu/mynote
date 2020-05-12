'''
we can actually use templates to have a “base” template and inherit that template in the .html files.
'''

#Relative URLs with Templates
#how to use various methods to pass relative URLs with Templates.
'''
We can easily fix this with the use of URLs in our templates. For example:
    <a href=”basicapp/thankyou”>Thanks</a>
Can be changed to:
    <a href=”{% url ‘thanku’%}”>Thanks</a>
name=‘thanku’ is in the urls.py file.

  <a href=”basicapp/thankyou”>Thanks</a>
Can be changed to:
  <a href=”{% url‘basicapp.views.thankyou’%}”>Thanks</a> 

suggested (and most future-proof) method to do all of this involves the urls.py file.
Inside the urls.py file  you add in the variable app_name
You then set this variable equal to a string that is the same as your app name

Using templates for relative URLs will really help with multiple applications.
'''

#example
#create templates/basic_app/base.html
#create templates/basic_app/index.html
    <h1>WELCOME TO INDEX</h1>
#create templates/basic_app/other.html
    <h1>WELCOME TO OTHER</h1>
#create templates/basic_app/relative_url_templates.html
    <h1>WELCOME TO RELATIVE URL TEMPLATE</h1>
    
    
#view.py
    from django.shortcuts import render
    # Create your views here.
    def index(request):
        return render(request,"basic_app/index.html",context_dict)
    def other(request):
        return render(request,"basic_app/other.html")
    def relative(request):
        return render(request,"basic_app/relative_url_templates.html")

#urls.py
    urlpatterns = [
        url(r'^$',views.index,name='index'),
        path('admin/', admin.site.urls),
        url(r'^basic_app/',include('basic_app.urls')),
    ]

#basic_app/urls.py
    from django.conf.urls import url
    from basic_app import views
    #TEMPLATE TAGGING
    app_name= 'basic_app'
    urlpatterns=[
        url(r'^relative/$',views.relative,name='relative'),
        url(r'^other/$',views.other,name='other'),
    ]
 
#relative_url_templates.html
    <body>
        <h1>WELCOME TO RELATIVE URL TEMPLATE</h1>
        <a href="{% url 'basic_app:other' %}">THE OTHER PAGE</a>
        <a href="{% url 'admin:index' %}">linke to admin</a>
        <a href="{% url 'index' %}">linke to index</a>
    </body>

'''
URL Template inheritance
Template inheritance allows us to create a base template we can inherit from.
Here are the main steps for inheritance:
    Find the repetitive parts of your project
    Create a base template of them
    Set the tags in the base template
    Extend and call those tags anywhere
base.html	
  <links to JS, CSS, Bootstrap>
  <bunch of html like navbars>
    <body>
      {% block body_block %}
      {% endblock %}
    </body>
  </More footer html>
other.html
  <!DOCTYPE html>
  {% extends "basic_app/base.html" %}
  {% block body_block%}  
  <HTML specific for other.html>
  <HTML specific for other.html>
  {% endblock %}
'''

#base.html
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
  </head>
  <body>
    <nav class="navbar navbar-default navbar-static-top">
      <div class="container">
        <ul class="nav navbar-nav">
          <li><a class="navbar-brand" href="{% url 'index' %}">brand</a></li>
          <li><a class="navbar-link" href="{% url 'admin:index' %}">Admin</a></li>
          <li><a class="navbar-link" href="{% url 'basic_app:other' %}">other</a></li>
        </ul>
      </div>
    </nav>

    <div class="container">
        {% block body_block %}
        <!--anything outside of this will be inherited-->
        {% endblock %}
    </div>
  </body>
</html>
 
#other.html
<!DOCTYPE html>
{% extends "basic_app/base.html"%}
  {% block body_block %}
    <h1>WELCOME TO OTHER</h1>
    <h2>this is an example of template inheritance</h2>
    {% endblock %}
    
#index.html
<!DOCTYPE html>
{% extends "basic_app/base.html" %}
  {% block body_block %}
      <h1>WELCOME TO INDEX</h1>
      <h1>This is index.html page showing</h1>
    {% endblock %}


'''
Imagine that you had some information from your model that you wished to use across various views/pages.
But perhaps you wanted to make a slight edit to the information before injecting it, like string operations, or arithmetic.
The general form for a template filter is:
    {{ value | filter:”parameter” }}
Not all filters take in parameters.
Many of these filters are based off of common built-in Python functions so you will be already familiar with them!
https://docs.djangoproject.com/en/2.1/topics/templates/#filters
'''
#step1:
#view.py
    def index(request):
        context_dict={'text':'hello word','number':100}
        return render(request,"basic_app/index.html",context_dict)

#step2:
#index.html
    <!DOCTYPE html>
    {% extends "basic_app/base.html" %}
      {% block body_block %}
          <h1>WELCOME TO INDEX</h1>
          <h1>This is index.html page showing</h1>
          <h1>{{ text|upper }}</h1>
          <h1>{{ number|add:'99' }}</h1>
      {% endblock %}

#step3: customer filters
#creat folder and file
#basic_app/templatetags
#basic_app/templatetags/__init__.py  : empty
#basic_app/templatetags/my_extras.py
    from django import template
    register = template.Library()
    @register.filter(name='cut')
    def cut(value, arg):
        '''
        this cut our all value of "arg" from string
        '''
        return value.replace(arg,'')
    #register.filter('cut',cut)

#step4
#index.html
    <!DOCTYPE html>
    {% extends "basic_app/base.html" %}
      {% block body_block %}
          <h1>{{ text|cut:'hello' }}</h1>
        {% endblock %}
