# 序列（sequence）
在Python中，最基本的数据结构为序列（sequence）。序列中的每个元素都有编号，即其位置或索引，其中第一个元素的索引为0，第二个元素的索引为1，依此类推  
最常用的序列有：列表和元组，字符串。

# 通用的序列操作
有几种操作适用于所有序列，包括索引、切片、相加、相乘和成员资格检查。另外，Python还提供了一些内置函数，可用于确定序列的长度以及找出序列中最大和最小的元素。

### 索引（indexing）
* 序列中的所有元素都有编号——从0开始递增。  
  * 注意：Python没有专门用于表示字符的类型，因此一个字符就是只包含一个元素的字符串。
```python
greeting="Hello"
x=greeting[0]  # 'H'
x=greeting[-1] # 'o'
```

* 如果函数调用返回一个序列，可直接对其执行索引操作。
```py
>>> fourth = input('Year: ')[3]
Year: 2005
>>> fourth
'5' 
```

### 切片（slicing）
* 切片适用于提取序列的一部分，其中的编号非常重要：第一个索引是包含的第一
个元素的编号，但第二个索引是切片后余下的第一个元素的编号
```py
>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numbers[3:6] [4, 5, 6]
>>> numbers[0:1] [1]
```

* 切片简写
```py
>>> numbers[7:10]  #[8, 9, 10]
>>> numbers[-3:-1] #[8, 9]
>>> numbers[-3:0]  #[] 
>>> numbers[-3:]   #[8, 9, 10]
>>> numbers[:3]    #[1, 2, 3]
```
* 切片复制
```py
>>> a=[1,2,3,4]
>>> b=a[:]
>>> c=a
>>> b[0]=2
>>> c[0]=3
>>> a #[3, 2, 3, 4]
>>> b #[2, 2, 3, 4]
>>> c #[3, 2, 3, 4]
```

* 步长
执行切片操作时，你显式或隐式地指定起点和终点，但通常省略另一个参数，即步长。在普
通切片中，步长为1。这意味着从一个元素移到下一个元素，因此切片包含起点和终点之间的所
有元素。   
```py
>>> numbers[0:10:1]  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> numbers[0:10:2]  #[1, 3, 5, 7, 9]
>>> numbers[3:6:3]   #[4] 
>>> numbers[::4]     #[1, 5, 9]
```
当然，步长不能为0，否则无法向前移动，但可以为负数，即从右向左提取元素。  
```py
>>> numbers[8:3:-1]   #[9, 8, 7, 6, 5]
>>> numbers[10:0:-2]  #[10, 8, 6, 4, 2]
>>> numbers[0:10:-2]  #[]
>>> numbers[::-2]     #[10, 8, 6, 4, 2] 
>>> numbers[5::-2]    #[6, 4, 2]
>>> numbers[:5:-2]    #[10, 8]
```

### 序列相加  
* 可使用加法运算符来拼接序列。  
```py
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> 'Hello,' + 'world!'
'Hello, world!'
>>> [1, 2, 3] + 'world!'
Traceback (innermost last):
 File "<pyshell>", line 1, in ?
 [1, 2, 3] + 'world!'
TypeError: can only concatenate list (not "string") to list
```

### 乘法
* 将序列与数x相乘时，将重复这个序列x次来创建一个新序列  
```py
>>> 'python' * 5
'pythonpythonpythonpythonpython'
>>> [42] * 10
[42, 42, 42, 42, 42, 42, 42, 42, 42, 42]
```

### 成员资格
* 要检查特定的值是否包含在序列中，可使用运算符in 
```py
>>> permissions = 'rw'
>>> 'w' in permissions  #True
>>> 'x' in permissions  #False
>>> users = ['mlh', 'foo', 'bar']
>>> input('Enter your user name: ') in users
Enter your user name: mlh
True
>>> subject = '$$$ Get rich now!!! $$$'
>>> '$$$' in subject    #True
```
*  检查用户名和PIN码
```py
database = [
 ['albert', '1234'],
 ['dilbert', '4242'],
 ['smith', '7524'],
 ['jones', '9843']
]
username = input('User name: ')
pin = input('PIN code: ')
if [username, pin] in database: print('Access granted')
```

### 长度、最小值和最大值
* 内置函数len、min和max  
```py
>>> numbers = [100, 34, 678]
>>> len(numbers)  #3
>>> max(numbers)  #678
>>> min(numbers)  #34
```