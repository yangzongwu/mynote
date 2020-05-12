#user_info.html
'''
增加<a href="/cmdb/userdel-{{ row.id }}">删除</a>
'''
'''
<h3>用户列表</h3>
        <ul>
            {% for row in user_list %}
                <li> <a href="/cmdb/userdetail-{{ row.id }}/">{{ row.username }}</a>|
                    <a href="/cmdb/userdel-{{ row.id }}">删除</a></li>
            {% endfor %}
        </ul>
'''

#urls.py
#新增一条URL：url(r'^userdel-(?P<nid>\d+)/',views.user_del),
'''
urlpatterns = [
    url(r'^index/',views.index,name='indexx'),
    url(r'^login/',views.login),
    url(r'^orm/',views.orm),
    url(r'^user_info/',views.user_info),
    url(r'^userdel-(?P<nid>\d+)/',views.user_del),
    url(r'^userdetail-(?P<nid>\d+)/',views.user_detail),
]
'''

#view.py
'''
def user_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info/')
'''
