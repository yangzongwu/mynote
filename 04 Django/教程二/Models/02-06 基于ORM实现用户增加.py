#user_info.html 
'''
<h3>添加用户</h3>
        <form method="POST" action="/cmdb/user_info/">
            <input type="text" name="user">
            <input type="text" name="pwd">
            <input type="submit" value="添加">
        </form>
'''

#views.py
'''
def user_info(request):
    if request.method=='GET':
        user_list=models.UserInfo.objects.all()
        #print(user_list.query)# 查看当前SQL语句
        return render(request, 'user_info.html',{'user_list':user_list})
    elif request.method=='POST':#添加功能
        u=request.POST.get('user')
        p=request.POST.get('pwd')
        models.UserInfo.objects.create(username=u,password=p)
        return redirect('/cmdb/user_info/')
        #user_list = models.UserInfo.objects.all()
        #return render(request, 'user_info.html', {'user_list': user_list})

'''
