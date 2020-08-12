### 文件操作
* 文件重命名
    * os.rename(old_name,new_name)
* 删除文件
    * os.remove(文件名)
    
### 文件夹操作
* 创建文件夹
    * os.mkdir(文件夹名)
* 删除文件夹
    * os.rmdir(文件夹名)
* 获取当前目录
    * os.getcwd()
* 改变默认目录
    * os.chdir(目录)
* 获取目录列表
    * os.listdir() # 当前目录下文件列表
    * os.listdir(目录) # 指定目录下文件列表
* 重命名文件夹
    * os.rename(原文件夹名，新文件夹名)