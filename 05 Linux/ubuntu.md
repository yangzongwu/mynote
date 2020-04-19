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

* 新建文件 命令为:
touch filename

Ø E: Unable to lock directory /var/lib/apt/lists/_在Ubuntu下解决E: 加锁的问题
错误提示：E: 无法获得锁 /var/lib/apt/lists/lock – open (11: 资源暂时不可用)
	• 运行下面的命令来生成所有含有 apt 的进程列表
	命令：ps -A| grep apt
	• 杀死进程
	命令：kill -9 2814


Ø Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
	• 因为没有切换管理员权限 
sudo su