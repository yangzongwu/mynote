'''
we use templates to insert simple text
how about other static media files, like photo 

First, we creat a new directory inside of the project called static
Then we will add this directory path to the project's settings.py file
Then we will add a STATIC_URL variable
'''

#build new file and folder
#first_project/static/css/mystyle.css
#first_project/static/images/google.jpg

#change templates/first_app/index.html
  <!DOCTYPE html>
  {% load staticfiles %}
  <html lang="en" dir="ltr">
    <head>
      <meta charset="utf-8">
      <title>Django page</title>
      <link rel="stylesheet" href="{% static "css/mystyle.css" %}"/>
    </head>
    <body>
      <h1>This is picture</h1>
      <img src="{% static "images/google.jpg" %}" alt="uh oh , did not show">
    </body>
  </html>
 
#change first_project/settings.py
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR=os.path.join(BASE_DIR,"static")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
