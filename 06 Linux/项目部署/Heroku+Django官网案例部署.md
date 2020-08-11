官方案例
# 配置服务器
* 下载安装Heroku  
https://devcenter.heroku.com/articles/heroku-cli
* 登录Heroku account
```
heroku login
```
# 本地创建应用
如下是官方推荐，建议进去修改其index.html，更明显知道是否部署成功
```
git clone https://github.com/heroku/python-getting-started.git
cd python-getting-started
pip install -r requirement #安装依赖库
```
# 部署应用
* 在Heroku创建一个app
```
heroku create xxx
```
* 部署代码
向远程库(heroku)推送本地的master分支
```
git push heroku master
```
* 运行实例
```
heroku ps:scale web=1
```
* 访问app
```
heroku open
```
* 查看日志
```
heroku logs --tail
```