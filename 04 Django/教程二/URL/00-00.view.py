from django.shortcuts import render,HttpResponse,redirect
from django.views import View

USER_DICT={
    '1':{'name':'root1','email':'root@live.com'},
    '2':{'name':'root2','email':'root@live.com'},
    '3':{'name':'root3','email':'root@live.com'},
    '4':{'name':'root4','email':'root@live.com'},
    '5':{'name':'root5','email':'root@live.com'}
}

def index(request):
    return render(request, 'index.html', {'user_dict':USER_DICT})

def detail(request):
    nid=request.GET.get('nid')
    detail_info=USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})

#---02---
def detail(request,nid):
    detail_info=USER_DICT[nid]
    return render(request,'detail.html',{'detail_info':detail_info})
   
