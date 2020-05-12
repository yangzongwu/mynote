#function base view  
#		urls.py
#			index -> 函数名
#			view.py
#			def 函数(request):
#				...
#		====》
#		/index/ -> 函数名
#		/index/ -> 类
#		====》


url.py
from app01 import views
from django.conf.urls import url,include
urlpatterns = [
    url(r'^home/',views.home),
    url(r'^home/',views.Home.as_view()),
]

view.py
# FBV
def home(requset):
    if request.method=='GET':
        return render(request,'home.html')
    elif request.method=='POST':
        return render(request,'home.html')
# CBV Class base view
class Home(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        return render(request, 'home.html')
        
        
class Home(View): 
    # dispatch优先执行，如果写了如下函数，后续get,post不执行
    # def dispatch(self, request, *args, **kwargs):
    #     return HttpResponse('ok')
    # 如果需要增加功能，用如下方法
    def dispatch(self, request, *args, **kwargs):
        #调用父类中的dispatch方法
        #每次调用get,post 都会执行print('before')，print('after')
        print('before')#自定义操作
        result=super(Home,self).dispatch(request, *args, **kwargs)
        print('after')#自定义操作
        return result
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        return render(request, 'home.html')
