from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo import forms
from AppTwo.forms import FormName
# Create your views here.
def index(request):
    my_dict={'insert_me':'hello I am from AppTwo/index.html'}
    return render(request,'AppTwo/index.html',context=my_dict)
    #return HttpResponse('<em>Goto /user to see user info.</em>')

def help(request):
    my_dict={'insert_me':'hello I am from AppTwo/index.html'}
    return render(request,'AppTwo/index.html',context=my_dict)

def user(request):
    User_list=User.objects.order_by('First_Name')
    my_dict={'user_info':User_list}
    return render(request,'AppTwo/user.html',context=my_dict)

def register(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)
        if form.is_valid():
            print("FIRSTNAME:"+form.cleaned_data['First_Name'])
            print("LASTNAME:"+form.cleaned_data['Last_Name'])
            print("EMAIL:"+form.cleaned_data['Email'])
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FROM INVALID")
    return render(request,'AppTwo/register.html',{'form':form})
