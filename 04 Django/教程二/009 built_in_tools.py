'''
We will focus mainly on the built-in tools:
    Users and the User Model
    Permissions
    Groups
    Passwords and Authentication
    Logging In and Out
'''

'''
Passwords
In this lecture we will discuss the general set-up to begin getting ready for User Authentication.
We’ll talk about passwords in general and also discuss some additional library options for security.
The first thing we need to take care of is setting up our ability to authenticate a User.
To do this we need to use some built-in apps and make sure they are under the INSTALLED_APPS list in settings.py
The apps we will use are “django.contrib.auth” and “django.contrib.contenttypes”
Often these will already be pre-loaded in the list for you.
Remember to migrate if you added them!
The next thing we need to do is make sure we store our passwords safely.
Never store passwords as plain text!
We will begin by using the default PBKDF2 algorithm with an SHA256 hash that is built-in to Django.
Django makes this really easy, we will also show how to use the bcrypt and Argon2.
In your virtual environment: 
    pip install bcrypt
    pip install django[argon2]
Inside of settings.py you can then pass in the list of PASSWORD_HASHERS to try in the order you want to try them.
If for some reason you don’t have the library support, eventually you will fall back on to the original PBKDF2
Sometimes users will also try to use a very weak password, such as “password123”.
We can also add in validator options to prevent a user from doing that.
We’ll keep things simple and only require a minimum length for now.

SHA-256
https://www.xorbin.com/tools/sha256-hash-calculator

In order to work with images with Python we will need to install the Python Imaging Library with:
    pip install pillow
Once you’ve created this model you’ll have to remember to register it in the admin.py file, with something like:
    admin.site.register(UserProfileInfo)
'''

#step 1:
    pip install bcrypt
    pip install django[argon2]

#step2:
#setting.py:
    # Password validation
    # https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    ]
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
            'OPTIONS':{'min_length':9}
        },
      ]
  
  
'''
In this lecture we will discuss how to use Django’s built in tools to create User Authorization Models.
We will also discuss how to set-up media files in your project.
The User object has a few key features:
    Username
    Email
    Password
    First Name
    Surname
There are also some other attributes for the User object, such as is_active, is_staff, is_superuser.
Sometimes you will also want to add more attributes to a user, such as their own links or a profile image.
You can do this in your applications models.py file by creating another class that has a relationship to the User class.

Notice a new field we haven’t seen yet, an ImageField. 
This will allow you to store images to a model, typically we will keep any user uploaded content like this in the media file.
In order to work with images with Python we will need to install the Python Imaging Library with:
    pip install pillow
Once you’ve created this model you’ll have to remember to register it in the admin.py file, with something like:
    admin.site.register(UserProfileInfo)
    
Typically images, CSS, JS, etc. all go in the static folder of your project, with the STATIC_ROOT variable path defined inside of settings.py
User uploaded content will go to the media folder, with the MEDIA_ROOT.

Next we will want to implement a Django form that the User can use to work with the website.
Let’s show an example of what this would look like inside the forms.py file of your application.
Let’s now code through the set-up of what we’ve discussed:
    User Model
    Media Directory
    Handling Images
    User Form
'''
#step1:
#basic_app/models.py
    from django.db import models
    from django.contrib.auth.models import User
    # Create your models here.
    class UserProfileInfo(models.Model):
        user=models.OneToOneField(User,on_delete=models.PROTECT)
        # additional
        profolio_site=models.URLField(blank=True)
        profile_pic=models.ImageField(upload_to='profile_pics',blank=True)
        def __str__(self):
            return self.user.username
#user ImageField
    pip install pillow
#step2:
#create lerning_usres/media/profile_pics
    # when user upload media will be in this folder

#step2:
#create lerning_usres/media/profile_pics

#step3:
#create basic_app/forms.py
    from django import forms
    from django.contrib.auth.models import User
    from basic_app.models import UserProfileInfo

    class UserForm(forms.ModelForm):
        password=forms.CharField(widget=forms.PasswordInput())
        class Meta():
            model=User
            fields=('username','email','password')

    class UserProfileInfoForm(forms.ModelForm):
        class Meta():
            model=UserProfileInfo
            fields=('profolio_site','profile_pic')

#step4:
#admin.py
    from django.contrib import admin
    from basic_app.models import UserProfileInfo
    # Register your models here.
    admin.site.register(UserProfileInfo)


#how to connect each other
#create lerning_usres/static
#setting.py
      STATIC_URL = '/static/'
      STATICFILES_DIR=[STATIC_DIR,]
#create lerning_usres/media
 #setting.py
      MEDIA_ROOT=MEDIA_DIR
      MEDIA_URL='/media/'

#step1:
#templates/base_app/base.html
  <body>
    <nav class="navbar navbar-default navbar-static-top">
      <div class="container">
        <ul class="nav navbar-nav">
          <li><a class="navbar-brand" href="{% url 'index' %}">Django home</a></li>
          <li><a class="navbar-link" href="{% url 'admin:index' %}">Admin</a></li>
          <li><a class="navbar-link" href="{% url 'basic_app:register' %}">Register</a></li
        </ul>
      </div>
    </nav>
    <div class="container">
      {% block body_block %}
      {% endblock %}
    </div>
  </body>

#step2:
#templates/base_app/index.html
    {% extends "basic_app/base.html" %}
    {% block body_block %}
    <div class="jumbtron">
      <h1>Django level Five</h1>
    </div>
    {% endblock %}

#step3:
#templates/base_app/registration.html
    {% extends "basic_app/base.html" %}
    {% load staticfiles %}
    {% block body_block %}
    <div class="jumbtron">
      {% if registered %}
        <h1>Thank you for registering</h1>
      {% else %}
        <h1>Register here!</h1>
        <h3>Fill out the form:</h3>
        <form enctype="multipart/form-data" method="post" >
            {% csrf_token %}
            {{ user_form.as_p }}
            {{ profile_form.as_p }}
            <input type="submit" name="" value="Register">
        </form>
      {% endif %}
    </div>
    {% endblock %}

#step4: urls
    urlpatterns = [
        url(r'^$',views.index,name='index'),
        url(r'^basic_app',include('basic_app.urls')),
    ]

#step5: basic_app/urls
    from django.conf.urls import url
    from basic_app import views
    #TEMPLATE URLS!
    app_name='basic_app'
    urlpatterns=[
        url(r'^register/$',views.register,name='register'),
        url(r'^user_login/$',views.user_login,name='login'),
    ]


#Registration
'''
A lot of the coding for working with Users and Authorization happens in the views.py file.
The basic idea is that we check if there is a POST request and then perform some sort of action based off that information.
Sometimes we will want to save that information directly to the database.
Other times, we will set commit=False so we can manipulate the data before saving it to the database.
'''

#view.py
    from django.shortcuts import render
    from basic_app.forms import UserForm,UserProfileInfoForm
    # Create your views here.
    # Create your views here.
    def index(request):
        return render(request,'basic_app/index.html')
    def register(request):
        registered=False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            profile_form=UserProfileInfoForm(data=request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user= user_form.save()
                user.set_password(user.password)
                user.save()
                profile=profile_form.save(commit=False)
                profile.user=user
                if 'profile_pic' in request.FILES:
                    profile.profile_pic=request.FILES['profile_pic']
                profile.save()
                registered=True
            else:
                print(user_form.errors,profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()
        return render(request,'basic_app/registration.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered})
    
'''
log in/log out
This process involves:
    Setting up the login views
    Using built-in decorators for access
    Adding the LOGIN_URL in settings
    Creating the login.html
    Editing the urls.py files
'''

#step1:
#setting.py
    LOGIN_URL='/basic_app/user_login'

#base.html
      <div class="container">
        <ul class="nav navbar-nav">
          {% if user.is_authenticated %}
            <li><a class="navbar-link" href="{% url 'logout' %}">logout</a> </li>
          {% else %}
            <li><a class="navbar-link" href="{% url 'basic_app:login' %}">login</a></li>
          {% endif %}
        </ul>
      </div>

#login.html
    {% extends 'basic_app/base.html' %}
    {% block body_block %}
    <div class="jumbtron">
        <h1>please login</h1>
        <form action="{% url 'basic_app:user_login' %}" method="post">
          {% csrf_token %}
          <label for="username">Username:</label>
          <input type="text" name="username" placeholder="enter username">
          <label for="password">Password:</label>
          <input type="password" name="password">

          <input type="submit" name="" value="Login">
        </form>
    </div>
    {% endblock %}

#view.py
    from django.contrib.auth import authenticate,login,logout
    from django.http import HttpResponseRedirect,HttpResponse
    #from django.core.urlresolvers import reverse
    from django.urls import reverse
    from django.contrib.auth.decorators import login_required
    @login_required
    def user_logout(request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    def user_login(request):
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')
            else:
                print('someone tr to login failed')
                print('username:{} and password: {}'.format(username,password))
                return HttpResponse('invalid login in')
        else:
            return render(request,'basic_app/login.html',{})

#urls
    urlpatterns = [
        url(r'^logout/$',views.user_logout,name='logout'),
        url(r'special/',views.special,name='special'),
    ]
 
 #basic_app/urls
    urlpatterns=[
        url(r'^register/$',views.register,name='register'),
        url(r'^user_login/$',views.user_login,name='login'),
    ]
 
