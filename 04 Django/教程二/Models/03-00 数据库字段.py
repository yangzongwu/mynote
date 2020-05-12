'''
class UserInfo(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    
    修改:
    password=models.CharField(max_length=60)
    超过部分删除
    
    删除数据：
    #password=models.CharField(max_length=64) 
    
    
    增加：
    gender=models.CharField(max_length=64，null=True)
    null=True默认空，不写需要写值
'''

#字符串，数字，时间，二进制
class UserInfo(models.Model):
    username=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    test=models.URLField(max_length=32)
    test=models.GenericIPField(max_length=32)
#Field是给django的admin判断的格式是否正确，
#如果自己写，都默认字符串，无影响


class UserGroup:
    uid = models.AutoField(primary_key=True)#创建自增列
    caption=models.CharField(max_lenth=32)
    #如果自己写了一个自增列，默认的id列不会创建，必须加上primary_key
    
    
 # 字段：
 # 字符串，数字，时间，二进制，自增
 
