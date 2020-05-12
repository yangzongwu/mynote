from django.db import models

# Create your models here.
'''
ORM操作
ORM里面有两类（主流是code firs）：
db first 自己创建数据库以及对应关系，用pycharm等链接数据库生成各种类，
code first 先写类代码，然后生成表

code first 创建类
1.根据类自动创建数据库表
    python manage.py makemigrations
    python manage.py migrate
2.根据类对数据库表中的数据进行各种操作
'''

class UserInfo(models.Model):
    #id列，自增，主键
    #创建用户名列，字符串类型，指定长度
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
'''
如上创建类，
1.创建类,class UserInfo(models.Model):username,password
2.setting里面增加环境变量INSTALLED_APPS
3.系统自动生成数据库到makemigrations：python manage.py makemigrations
4.系统自动生成数据库到db.sqlite:python manage.py migrate
5.默认的表名为：app01_userinfo
6.该表有一列自动的自增列id，并且是主键
'''

'''
********** 注意 ***********
Django默认使用MySQLdb模块链接MySQL
主动修改为pymysql，在project同名文件夹下的__init__文件中添加如下代码即可：
import pymysql
pymysql.install_as_MySQLdb()
'''

'''
setting 里面默认sqlite3，可以修改链接其他数据库
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
