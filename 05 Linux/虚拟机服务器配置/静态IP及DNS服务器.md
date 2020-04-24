# VMware配置网络环境
VMware在默认安装完成之后，会创建三个虚拟的网络环境：
* VMnet0--桥接网络
* VMnet1--Host-only
* VMnet8--NAT

### NAT配置
* click "open VMware"-->"edit"-->"Virtual Network Editor"-->"change setting"
* choose VMnet8
    * subnetIP 子网：192.168.28.0
    * 子网掩码：255.255.255.0
* NAT setting:
    * GatewayIP 网关:192.168.28.2
* 取消“User local DHCP service to distribute IP address to VMs”

### 虚拟机
setting里面的网络适配器选择“自定义”-->“VMnet8(NAT模式)”

# Ubuntu设置
### 设置静态IP地址
network setting-->wired-->add  
New profile-->Identity-->name: ens33  
New profile-->IPv4  
* choose "Manual"
* Address:192.168.28.* (* 0~255)
* Netmask:255.255.255.0
* Getway:192.168.28.2
###　配置interfaces文件
```
sudo gedit /etc/network/interfaces
```
```
auto lo
iface lo inet loopback

auto ens33
iface ens33 inet static
address 192.168.8.100
netmask 255.255.255.0
gateway 192.168.8.2
```
###　配置DNS服务器
```
sudo gedit /etc/resolv.conf
```
```
nameserver 223.5.5.5
nameserver 114.114.114.114
```
### 重启网络
```
sudo /etc/init.d/networking restart
```
###　报错处理
* 无法启动网络显示“device not managed”
```
sudo gedit /etc/NetworkManager/NetworkManager.conf
```
打开该文件，将“managed=false”修改为“managed=true”。
```
sudo service network-manager restart
```