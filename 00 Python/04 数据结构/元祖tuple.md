# 元组：不可修改的序列tuple
与列表一样，元组也是序列，唯一的差别在于元组是不能修改的（你可能注意到了，字符串
也不能修改）。元组语法很简单，只要将一些值用逗号分隔，就能自动创建一个元组。    
列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组  


### 组的表示
* 元组还可用圆括号括起（这也是通常采用的做法）
```py
>>> 1, 2, 3
(1, 2, 3)
```
* 如何表示只包含一个值的元组呢？  
这有点特殊：虽然只有一个值，也必须在它后面加上逗号。   
```py
>>> 42  #42
>>> 42, #(42,) 
>>> 3 * (40 + 2)    #126
>>> 3 * (40 + 2,)   #(42, 42, 42)
```

```py
>>> tuple([1, 2, 3])
(1, 2, 3)
>>> tuple('abc')
('a', 'b', 'c')
>>> tuple((1, 2, 3))
(1, 2, 3)
```


### 元组的索引
定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
```python
dimensions=(200,50)
print(dimensions[0])#200
print(dimensions[1])#50
```
遍历元组中的所有值
```python
dimensions=(200,50)
for dimension in dimensions:
     print(dimension)
```


### 元组的修改
由于试图修改元组的操作是被禁止的，因此Python指出不能给元组的元素赋值：
```
Traceback(mostrecentcalllast):
    File"dimensions.py",line3,in<module>
    dimensions[0]=250
    TypeError:'tuple'objectdoesnotsupportitemassignment
```
* 修改元组变量  
虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组：  
```
dimensions=(200,50)
print("Originaldimensions:")
for dimension in dimensions:
    print(dimension)    #200,50
dimensions=(400,100)
print("\nModifieddimensions:")
for dimension in dimensions:
    print(dimension)    #400,100
```
