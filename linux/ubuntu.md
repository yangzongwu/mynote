# pycharm
### 安装pycharm
* 进入指定目录
```
cd ～/Downloads/pycharm/bin
```
* 安装
```
sh ./pycharm.sh
```
### 启动pycharm
* 进入指定目录
```
cd pycharm/bin
```
* 启动
```
sh pycharm.sh
```

# 查IP
```
sudo apt-get install net-tools  
ifconfig
```


使用sudo apt-get update命令时出现如下错误：  
```
E: Could not get lock /var/lib/apt/lists/lock - open (11: Resource temporarily unavailable)
E: Unable to lock directory /var/lib/apt/lists
```
解决办法：    
```
sudo rm /var/lib/apt/lists/lock
```

在 ubuntu 中新建文件夹 命令为:

mkdir folder-name
在 ubuntu 中 新建文件 命令为:

touch filename