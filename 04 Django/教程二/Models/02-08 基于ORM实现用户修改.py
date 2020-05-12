#user_info.html
#增加 <a href="/cmdb/useredit-{{ row.id }}">编辑</a>
'''
<h3>用户列表</h3>
        <ul>
            {% for row in user_list %}
                <li> <a href="/cmdb/userdetail-{{ row.id }}/">{{ row.username }}</a>|
                    <a href="/cmdb/userdel-{{ row.id }}">删除</a>|
                    <a href="/cmdb/useredit-{{ row.id }}">编辑</a>
                </li>
            {% endfor %}
        </ul>
'''

#urls.py
#增加 url(r'^useredit-(?P<nid>\d+)/',views.user_edit),
'''
urlpatterns = [
    url(r'^index/',views.index,name='indexx'),
    url(r'^login/',views.login),
    url(r'^orm/',views.orm),
    url(r'^user_info/',views.user_info),
    url(r'^userdel-(?P<nid>\d+)/',views.user_del),
    url(r'^useredit-(?P<nid>\d+)/',views.user_edit),
    url(r'^userdetail-(?P<nid>\d+)/',views.user_detail),
]
''

#view.py
'''
def user_edit(request,nid):
    if request.method=='GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    elif request.method=='POST':
        nid=request.POST.get('id')
        u=request.POST.get('username')
        p=request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/cmdb/user_info/')
'''

#user_edit.html
'''
<form method="POST" action="/cmdb/useredit-{{ obj.id }}/">
        <input style="display:none" type="text" name="id" value={{ obj.id }}>
        <input type="text" name="username" value={{ obj.username }}>
        <input type="text" name="password" value={{ obj.username }}>
        <input type="submit" value="提交">
    </form>
'''
