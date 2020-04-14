# 建立第一个应用blog
* python manage.py startapp blog 
* setting 注册blog

# 配置访问路径
* my_site/urls
* blog/urls

# 配置数据库
数据库：作者，标题，正文，创建时间，修改时间
排序方式，返回值
数据迁移
* python manage.py makemigrations
* python manage.py migrate

# 把数据库注册到后台
admin.py
```python
admin.site.register(Blog)
```

