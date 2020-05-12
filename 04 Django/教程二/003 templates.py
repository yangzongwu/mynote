'''
The template will contain the static parts of an html page 

Then there are template tags, which have their own specil syntax
This syntax allow you to inject dynamic content that your Django App.view will 
produce, effecting the final HTML
'''

#first_prject/first_project/settings.py
  import os
  # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
  TEMPLATE_DIR=os.path.join(BASE_DIR,"templates")
  
  #add templates path to 'DIR
  TEMPLATES = [
      {
         'DIRS': [TEMPLATE_DIR,],
      }

#first_prject/first_app/views.py
  from django.shortcuts import render # this is new render function
  from django.http import HttpResponse
  # Create your views here.
  def index(request):
      my_dict={'insert_me':"Hello I am from first_app/index.html!"}
      return render(request,'first_app/index.html',context=my_dict)
      
#build new file and folder
#first_project/templates/first_app/index.html
  <!DOCTYPE html>
  <html lang="en" dir="ltr">
    <head>
      <meta charset="utf-8">
      <title>First App</title>
    </head>
    <body>
      <h1>Hello this is index.html!</h1>
      {{ insert_me }}
    </body>
  </html>

