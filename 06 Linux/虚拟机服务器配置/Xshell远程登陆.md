# SSH程序的安装
确保在服务器上安装好了openssh-server程序，在本地主机上安装好了openssh-client程序。
```
sudo apt install openssh-client #本地主机运行此条，实际上通常是默认安装client端程序的
sudo apt install openssh-server #服务器运行此条命令安装
```
# 服务器启动ssh服务
般服务器上安装ssh完成后，会自动启动ssh服务，并且默认随系统启动，如果没有，请手动启动
```
sudo /etc/init.d/ssh start #服务器启动ssh-server服务，
sudo /etc/init.d/ssh stop #server停止ssh服务
sudo /etc/init.d/ssh restart #server重启ssh服务
```
# 在本地主机端ssh远程登录服务器
这一步需要知道服务器的用户名(我的服务器名字也是yzw及IP地址。  
在本地主机上运行以下命令：  
用户端连接服务器用于登录远程桌面(以下user时远程主机的用户名)  
```
ssh yzw@192.168.28.128
```

# 退出远程登录
用Ctrl+D或者
```
exit
```