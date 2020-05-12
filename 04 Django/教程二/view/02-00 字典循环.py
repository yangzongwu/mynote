from django.shortcuts import render,HttpResponse,redirect
from django.views import View


# Create your views here.
# USER_DICT1={'1':'root1','2':'root2','3':'root3'}
# HTML 如何处理？和python字典一样，有keys,values,items但是后面不加（）
# { %for k, row in user_dict.items %}
# < li > {{k}} - -{{row}} < / li >
# { % endfor %}
#{ %for k in user_dict.keys %}
# < li > {{k}}  < / li >
# { % endfor %}
#{ %for k in user_dict.values %}
# < li > {{k}} < / li >
# { % endfor %}
