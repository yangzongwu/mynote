### 安装
直接使用pip安装就可以了
```
sudo pip install uwsgi
```

### 报错
* 安装过程中如果出现Exception: you need a C compiler to builduWSGI
是因为服务器上没有c编译器，先安装
```
apt-get install gcc
```

* 出现错误 fatal error: Python.h: No such file or directory compilation terminated.
```
apt install python3-dev
```

### 测试
安装完成测试是否安装正常
```
uwsgi --version
```