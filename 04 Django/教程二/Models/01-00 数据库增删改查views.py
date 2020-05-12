urls.py
urlpatterns = [
    url(r'^orm/',views.orm),
]


from app01 import models
def orm(request):
    #创建数据1
    models.UserInfo.objects.create(username='root',password='123',)
    # 创建数据2
    dic = {'username': 'eric', 'password': '666'}
    models.UserInfo.objects.create(**dic)
    # 创建数据3
    obj=models.UserInfo(username='root1',password='123',)
    obj.save()


    # 查找数据
    result=models.UserInfo.objects.all()
    print(result)
    #result 是QuerySet(Django提供)类型，可以当作是一个列表
    #[obj(id,username,password),obj,obj]
    for row in result:
        print(row.id,row.username,row.password)

    result = models.UserInfo.objects.filter(username='root')
    result = models.UserInfo.objects.filter(username='root',password='123')
    #也是一个QuerySet
    #filter相当于where


    #删除数据
    models.UserInfo.objects.all().delete()
    models.UserInfo.objects.filter(id=4).delete()


    #更新数据
    models.UserInfo.objects.all().update(password='999')
    models.UserInfo.objects.all(id=3).update(password='999')


    return HttpResponse('orm')
