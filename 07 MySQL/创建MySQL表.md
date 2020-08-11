创建数据库
```
mysql>create database xxx charset=utf8;
```
查看所有数据库
```
mysql>show databases;
```
选择数据库
```
mysql>use xxx;
```
查看数据库所有表
```
mysql>show tables;
```
查看当前使用的是哪个数据库
```
mysql>select database();
```
查看当前表的结构
```
mysql>show columns from cart;
```
创建数据表
```
CREATE TABLE IF NOT EXISTS Blog(
   author varchar(20),
   content varchar(200)
);
```