'''
表和表直接的关系
'''
class UserGroup(models.Model)
    uid = models.AutoField(primary_key=True)
    caption=models.CharField(max_lenth=32)
    createtime=models.DateTimeField(auto_now=True,null=True)
    updatetime=models.DateTimeField(auto_now_add=True,null=True)
    
class UserInfo(models.Model)
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    user_group=modes.ForeignKey('UserGroup',to_filed='uid',default=1)
    #Django生成的 user_group_id

user_list=UserInfo.objects.all()
for row in user_list:
    print(row.user_group_id)
    print(row.user_group.caption)
    #user_group是一个对象
'''
用户组：
uid   name
 1    DBA
 2    CEO
 
用户：
 id   用户名   密码    用户组ID
 1     alex    123       1
'''
