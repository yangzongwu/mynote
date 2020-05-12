通过名称来访问其各个值的数据结构。这种数据结构称为映射（mapping）。字典是Python中唯一
的内置映射类型，其中的值不按顺序排列，而是存储在键下。键可能是数、字符串或元组。  

# 创建和使用字典
字典由键及其相应的值组成，这种键值对称为项（item）。在前面的示例中，键为名字，而
值为电话号码。每个键与其值之间都用冒号（:）分隔，项之间用逗号分隔，而整个字典放在花
括号内。空字典（没有任何项）用两个花括号表示，类似于下面这样：{}。  
在字典（以及其他映射类型）中，键必须是独一无二的，而字典中的值无需如此。  
```py
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'} 
```

### 函数 dict
可使用函数dict①从其他映射（如其他字典）或键值对序列创建字典。  
```py
>>> items = [('name', 'Gumby'), ('age', 42)]
>>> d = dict(items)
>>> d
{'age': 42, 'name': 'Gumby'}
>>> d['name']
'Gumby'
```
还可使用关键字实参来调用这个函数，如下所示：  
```
>>> d = dict(name='Gumby', age=42)
>>> d
{'age': 42, 'name': 'Gumby'} 
```

### 基本的字典操作
* len(d)返回字典d包含的项（键值对）数。
* d[k]返回与键k相关联的值。
* d[k] = v将值v关联到键k。
* del d[k]删除键为k的项。
* k in d检查字典d是否包含键为k的项。

# 字典方法
### clear
方法clear删除所有的字典项，这种操作是就地执行的（就像list.sort一样），因此什么都不
返回（或者说返回None）。  
```py>>> x = {}
>>> y = x
>>> x['key'] = 'value'
>>> y
{'key': 'value'}
>>> x.clear()
>>> y
{} 
```

### copy
方法copy返回一个新字典，其包含的键值对与原来的字典相同（这个方法执行的是浅复制，
因为值本身是原件，而非副本）。  
```py
>>> x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
>>> y = x.copy()
>>> y['username'] = 'mlh'
>>> y['machines'].remove('bar')
>>> y
{'username': 'mlh', 'machines': ['foo', 'baz']}
>>> x
{'username': 'admin', 'machines': ['foo', 'baz']}
```
为避免这种问题，一种办法是执行深复制，即同时复制值及其包含的所有值，等等。为此，
可使用模块copy中的函数deepcopy。  
```py
>>> from copy import deepcopy
>>> d = {}
>>> d['names'] = ['Alfred', 'Bertrand']
>>> c = d.copy()
>>> dc = deepcopy(d)
>>> d['names'].append('Clive')
>>> c
{'names': ['Alfred', 'Bertrand', 'Clive']}
>>> dc
{'names': ['Alfred', 'Bertrand']} 
```

### fromkeys
方法fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None。  
```py
>>> {}.fromkeys(['name', 'age'])
{'age': None, 'name': None} 
```
这个示例首先创建了一个空字典，再对其调用方法fromkeys来创建另一个字典，这显得有点
多余  
```py
>>> dict.fromkeys(['name', 'age'])
{'age': None, 'name': None}
```
如果你不想使用默认值None，可提供特定的值  
```py
>>> dict.fromkeys(['name', 'age'], '(unknown)')
{'age': '(unknown)', 'name': '(unknown)'}
```

### get
方法get为访问字典项提供了宽松的环境。通常，如果你试图访问字典中没有的项，将引发
错误。使用get来访问不存在的键时，没有引发异常，而是返回None。  
```py
>>> d = {}
>>> print(d['name'])
Traceback (most recent call last):
 File "<stdin>", line 1, in ?
KeyError: 'name'
>>> print(d.get('name'))
None
```
你可指定“默认”值，这样将返回你指定的值而不是None。    
```py
>>> d.get('name', 'N/A')
'N/A' 
```

### items
方法items返回一个包含所有字典项的列表，其中每个元素都为(key, value)的形式。字典项
在列表中的排列顺序不确定。  
```py
>>> d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
>>> d.items()
dict_items([('url', 'http://www.python.org'), ('spam', 0), ('title', 'Python Web Site')])
```

### keys
方法keys返回一个字典视图，其中包含指定字典中的键。  

### pop
方法pop可用于获取与指定键相关联的值，并将该键值对从字典中删除。  
```py
>>> d = {'x': 1, 'y': 2}
>>> d.pop('x')
1
>>> d
{'y': 2}
```

### popitem
方法popitem类似于list.pop，但list.pop弹出列表中的最后一个元素，而popitem随机地
弹出一个字典项，因为字典项的顺序是不确定的，没有“最后一个元素”的概念。如果你要以高效
地方式逐个删除并处理所有字典项，这可能很有用，因为这样无需先获取键列表。  
```py
>>> d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
>>> d.popitem()
('url', 'http://www.python.org')
>>> d
{'spam': 0, 'title': 'Python Web Site'} 
```

### setdefault
方法setdefault有点像get，因为它也获取与指定键相关联的值，但除此之外，setdefault
还在字典不包含指定的键时，在字典中添加指定的键值对。如果没有指定，默认为None。    
```py
>>> d = {}
>>> d.setdefault('name', 'N/A')
'N/A'
>>> d
{'name': 'N/A'}
>>> d['name'] = 'Gumby'
>>> d.setdefault('name', 'N/A')
'Gumby'
>>> d
{'name': 'Gumby'}
```

### update
方法update使用一个字典中的项来更新另一个字典。对于通过参数提供的字典，将其项添加到当前字典中。如果当前字典包含键相同的项，就替
换它。  
```py
>>> d = {
... 'title': 'Python Web Site',
... 'url': 'http://www.python.org',
... 'changed': 'Mar 14 22:09:15 MET 2016'
... } 
>>> x = {'title': 'Python Language Website'}
>>> d.update(x)
>>> d
{'url': 'http://www.python.org', 'changed':
'Mar 14 22:09:15 MET 2016', 'title': 'Python Language Website'} 
```

### values
方法values返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的视
图可能包含重复的值。  
```py
>>> d = {}
>>> d[1] = 1
>>> d[2] = 2
>>> d[3] = 3
>>> d[4] = 1
>>> d.values()
dict_values([1, 2, 3, 1]) 
```
