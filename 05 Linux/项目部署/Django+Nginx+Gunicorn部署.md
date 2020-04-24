推荐阅读 [Setting up Django and your web server with uWSGI and nginx](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#configure-nginx-for-your-site)
# ubuntu 系统配置
* 更新系统
```
sudo apt-get update
sudo apt-get upgrade
```
* 安装包
```
sudo apt-get install python3
sudo apt-get install python3-pip
```

# 项目文件配置
* 修改Django配置文件settings.py
```python
# mysite/settings.py
# 关闭调试模式
DEBUG = False
# 允许的服务器
ALLOWED_HOSTS = ['*']#修改为域名或者IP
# 静态文件收集目录
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
* 拉取配置文件
本地项目目录
```
pip freeze > requirements.txt
```

# GitHub 中拉取项目
* 选择进入相关文件夹下载项目文件
```
sudo apt-get install git
cd **/**
git clone https://https://github.com/yangzongwu/mysite.git
```
* 相关目录创建虚拟环境,并激活
```
sudo pip3 install virtualenv
virtualenv --python=python3 env
source env/bin/activate
```
* 安装库
```
cd mysite
(env) ../mysite$ pip3 install -r requirements.txt
(env) ../mysite$ python3 manage.py collectstatic
(env) ../mysite$ python3 manage.py migrate
```

# Nginx
```
sudo apt-get install nginx
```
可以直接修改/etc/nginx/sites-enabled/default文件
```
cd /etc/nginx/sites-enabled/
sudo vi default
```
```
server {
    listen      80;
    server_name 192.168.3.129;
    charset     utf-8;


    location /static {
        alias /home/yzw/test/uwsgi-tutorial/mysite/mysite/static;
    }

    location /media {
        alias /home/yzw/test/uwsgi-tutorial/mysite/mysite/media;
    }

    location / {
        proxy_set_header Host $host;
        proxy_pass http://unix:/tmp/192.168.3.129.socket;
    }
}
```
重启或者启动
```
sudo /etc/init.d/nginx start
sudo /etc/init.d/nginx restart
```
关闭相关端口进程
```
sudo fuser -k 80/tcp
```

# Gunicorn测试
返回项目环境
```
cd mysite
(env) ../mysite$ pip3 install gunicorn
(env) ../mysite$ sudo /etc/init.d/nginx restart
(env) ../mysite$ gunicorn --bind unix:/tmp/192.168.3.129.socket mysite.wsgi:application
```

# 后期运维
```
git pull origin master
python3 manage.py collectstatic
python3 manage.py migrate
# 重启 gunicorn
pkill gunicorn
gunicorn --bind unix:/tmp/192.168.3.129.socket mysite.wsgi:application
```