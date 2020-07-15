# 安装
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
```
### 初识
```python
# 数组
a = [[1, 2, 3], [4, 5, 6]]# [[1, 2, 3], [4, 5, 6]]
import numpy as np
b = np.array(a) #[[1 2 3]
                # [4 5 6]]
print("ndim:", b.ndim) # 维度 2
print("shape:", b.shape) # 形状 (2,3)
print("size:", b.size) # 多少元素 6
```

# 创建numpy
### 设置数据类型
一般我们定义的元素类型为浮点类型np.float和整型np.int
```
import numpy as np
a = [[1, 2, 3], [4, 5, 6]]
b = np.array(a)
b = np.array(a, dtype=np.float)
```

### 特殊矩阵
```python
import numpy as np
np.zeros((3,4)) #全0矩阵
#[[ 0.  0.  0.  0.]
# [ 0.  0.  0.  0.]
# [ 0.  0.  0.  0.]]
np.ones((3, 4), dtype=np.float) # 全1矩阵
np.empty((3, 4), np.float) #生成接近于0的数组，np.empty()用于生成接近于0的随机数数组
np.arange(10, 20, 2) #生成有序的数列或数组
np.arange(12).reshape(3, 4) #改变数组形状
a = np.linspace(1, 10, 20) #生成线段 生成从1开始到10，总共有20个数等距的数列
```

# 基本运算
### 加减乘除
```python
import numpy as np
a = np.array([10, 20, 30, 40]) #[10,20,30,40]
b = np.arange(4) #[0,1,2,3]
c = a + b #[10,21,32,43]
d = a + 4 #[14,24,34,44]
```

### 点乘和叉乘
向量：u=(u1,u2,u3) v=(v1,v2,v3)  
点积公式：u * v = u1v1+u2v2+u3v33=lul * lvl * COS(U,V)  
叉积公式：u x v = { u2 * v3 - v2 * u3, u3 * v1 - v3 * u1, u1 * v2 - u2 * v1}  
```python
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.dot(a, b) # 1*4+2*5+3*6=32
d = np.array([[1, 2, 3],
             [4, 5, 6]])
e = np.array([[1, 4],
             [2, 5],
             [3, 6]])
f = np.dot(a, b)# [[14 32]
                #  [32 77]]
```
numpy中可以用np.dot()函数来同时处理点积和叉积的运算。当输入部分是两个一维数组时，np.dot()就是点积操作，当输入部分是两个二维数组时，进行的就是叉积操作

### N次方
```python
a = np.array([1, 2, 3, 4])
b = a ** 2 # [1,4,9,16]
```

### 三角函数
```python
a = np.array([1, 2, 3, 4])
b = np.sin(a)
```

### 数组同数值比较
```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a<3) # [ True  True False False False]
```

### 生成随机数
输出0-1之间的随机数：
```python
a = np.random.random((3, 2))
```
### 矩阵基本运算
```python
a = np.array([[10, 30, 15],
              [20, 5, 25]])
np.sum(a)
np.min(a)
np.max(a)
a.sum(axis=0) # [25 35 45]# 列求和 
a.sum(axis=1) # [30 75]# 行求和 

print("最小值索引:", a.argmin())  #4
print("最大值索引:", np.argmax(a)) #1
print("平均值:", a.mean())
print("行平均值:", a.mean(axis=1))

a = np.array([10, 30, 15, 20, 5, 25])
print("累积求和:", a.cumsum()) # [ 10  40  55  75  80 105]
print("累差:", np.diff(a)) # [20,-15,5,-15,20]
```

### 找出非0的数
```python
a = np.array([[4, 0, 9],
              [1, 0, 8]])
np.nonzero(a) # (array([0, 0, 1, 1], dtype=int64), array([0, 2, 0, 2], dtype=int64))
```

### 排序转置
```python
a = np.array([[4, 0, 9],
              [1, 0, 8]])
np.sort(a) #  [[0,4,9],
           #   [0,1,8]] 
np.transpose(a) # 转置
```

### 截取矩阵中的数据
把矩阵中的数改变成只属于某个数据范围内的数，比3小的数被修改成了3，比7大的数被修改成了7
```python
a = np.array([[4, 0, 9],
              [1, 0, 8]])
np.clip(a, 3, 7)  #  [[4,3,7],
                  #   [3,3,7]] 
```


# 索引
```python
a = np.arange(3, 15).reshape(3, 4)
#[[ 3  4  5  6]
# [ 7  8  9 10]
# [11 12 13 14]]
print("第2行的数据:", a[2]) #[11 12 13 14]
print("第2行第3列的数据:", a[2][3]) # 14
print("第2行所有数:", a[2, :]) # [11 12 13 14]
print("第1列所有数:", a[:, 1]) #[4 8 12]
print("第1行从第2列到第4列的值:", a[1, 2:4]) # [9 10]
#把数据变平
a.flatten() #[ 3  4  5  6  7  8  9 10 11 12 13 14]
```

# 合并
```python
a = np.array([1, 1, 1])
b = np.array([2, 2, 2])
print(np.vstack((a, b))) # 上下合并
                         # [[1 1 1]
                         #  [2 2 2]]
print(np.hstack((a, b))) # [1 1 1 2 2 2]
print("a和b垂直合并：")
print(np.concatenate((a, b), axis=0))
print("a和b水平合并：")
print(np.concatenate((a, b), axis=1))
```

### 添加维度
```python
import numpy as np
a = np.array([1, 2, 3])
print(a[np.newaxis, :]) # [[1 2 3]]
print(a[:, np.newaxis]) #[[1]
                        # [2]
                        # [3]]
```

### 分割
```python
import numpy as np
a = np.arange(24).reshape(6, 4)
print("a=")
print(a)

print(np.split(a, 3, axis=0))    # 横向进行切割
print(np.split(a, [3, 5], axis=0)) #在第3行和第5行出进行切割
print(np.split(a, 2, axis=1)) #纵向分割数组
print(np.hsplit(a, 2)) # 垂直分割
print(np.vsplit(a, 2)) 水平分割
```

### 复制
```python
a = np.array([0, 1, 2, 3])
b = a
c = a.copy()
a[0] = 5
print(b is a) #True
print(c is a) #False
```