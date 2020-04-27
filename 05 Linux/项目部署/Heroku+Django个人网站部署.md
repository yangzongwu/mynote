# 建立django 项目
（略）

# Django配置
* Procfile文件  
在项目文件夹下新建Procfile文件，注意无后缀     
文件内容：gunicorn mysite.wsgi --log-file -    
其中mysite就是你的项目名 
 
* 数据库配置  
heroku 只支持postgrespool数据库  
```
# django-settings.py
import dj_database_url
DATABASES['default'] = dj_database_url.config()
```
然后 在git push后进行数据库创建
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```

* 静态文件配置
```
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
STATIC_ROOT = 'staticfiles'  
STATIC_URL = '/static/'  
STATICFILES_DIRS = (  
    os.path.join(BASE_DIR, 'static'),  
)  
```

* 生成 requirements.txt 文件  
pip3 freeze > requirements.txt


# 配置Heroku
* 下载安装Heroku  
https://devcenter.heroku.com/articles/heroku-cli
* 登录Heroku account
```
heroku login
```

# 本地创建应用
```
git clone https://github.com/yangzongwu/mysite.git
cd mysite
cd mysite　#我的项目有两层
pip install -r requirements.txt #安装依赖库
```

# 部署
### 登陆
```
$ heroku login
```
### 在Heroku创建一个app
```
heroku create xxx
```
### git管理与部署
* Create a new Git repository  
Initialize a git repository in a new or existing directory  
```
$ cd my-project/
$ git init
$ heroku git:remote -a appname(xxx)
```
* Deploy your application  
Commit your code to the repository and deploy it to Heroku using Git.  
```
$ git add . 
$ git commit -am "make it better"
$ git push heroku master
```
* Existing Git repository
For existing repositories, simply add the heroku remote
```
$ heroku git:remote -a appname(xxx)
```
### 部署代码
向远程库(heroku)推送本地的master分支
```
git push heroku master
```
### 运行实例
```
heroku ps:scale web=1
```
### 访问app
```
heroku open
```
### 查看日志
```
heroku logs --tail
```