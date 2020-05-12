
# request.POST
# request.GET
# request.FILES

# 单选request.POST.get
# 多选（checkbox）request.POST.getlist

# 文件上传，form标签特殊设置
# obj=request.FILES.get('fff')  
#      f=open(obj.name, mode='wb')
#      for i in obj.chunks():
#          f.write(i)
#      f.close()



def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        #get是单选，getlist多选
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        v = request.POST.get('gender')
        r = request.POST.getlist('favor') #checkbox
        s = request.POST.get('city')
        s2 = request.POST.getlist('city')
        f = request.POST.get('fff')
        print(u, p, v, r, s, s2, f)
 else:
        # PUT,DELETE,HEAD,OPTION...
        return redirect('/index/')
        
#文件上传
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        #上传文件，需要改变HTML form enctype，不加的时候默认上传是字符串
        #把文件加到file下面，其他加到POST下面
        #<form action="/login/" method="POST">
        #<form action="/login/" method="POST" enctype="multipart/form-data">
        
        f = request.POST.get('fff')  #文件名
        #<input type="file" name="fff">
        obj=request.FILES.get('fff')  
        print(obj,type(obj),obj.name) #obj指向文件对象，obj.name输出文件名
        
        import os
        file_path=os.path.join('upload',obj.name) #upload路径
        f=open(file_path, mode='wb')
        for i in obj.chunks():
            f.write(i)
        f.close()
        return render(request, 'login.html')
   else：
        pass
