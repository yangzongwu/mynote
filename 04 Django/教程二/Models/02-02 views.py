from django.shortcuts import render,HttpResponse,redirect
from django.views import View


def index(request):
    return render(request,'index.html')

def user_info(request):
    user_list=models.UserInfo.objects.all()
    #print(user_list.query)# 查看当前SQL语句
    return render(request, 'user_info.html',{'user_list':user_list})

def user_detail(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    #models.UserInfo.objects.get(id=nid)  可以取单条数据，但是容易报错需要try一下
    return render(request,'user_detail.html',{'obj':obj})
