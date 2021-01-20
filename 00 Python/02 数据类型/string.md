字符串就是一系列字符。在Python中，用引号括起的f都是字符串，其中的引号可以是单引号，也可以是双引号，
```
str1 = "Thisisastring."
str2 = 'Thisisalsoastring.'
str3 = 'Itoldmyfriend,"Pythonismyfavoritelanguage!"'
str4 = "Thelanguage'Python'isnamedafterMontyPython,notthesnake."
str5 = "OneofPython'sstrengthsisitsdiverseandsupportivecommunity."
```

## 字符串基本操作
所有标准序列操作（索引、切片、乘法、成员资格检查、长度、最小值和最
大值）都适用于字符串，但别忘了字符串是不可变的，因此所有的元素赋值和切片赋值都是非
法的。  

## 设置字符串的格式
以前，主要的解决方案是使用字符串格式设
置运算符——百分号。这个运算符的行为类似于C语言中的经典函数printf：在 % 左边指定一个字
符串（格式字符串），并在右边指定要设置其格式的值。指定要设置其格式的值时，可使用单个
值（如字符串或数字），可使用元组（如果要设置多个值的格式），还可使用字典（这将在下一章
讨论），其中最常见的是元组。
```
>>> format = "Hello, s. s enough for ya?"  %   %
>>> values = ('world', 'Hot')
>>> format values  %

'Hello, world. Hot enough for ya?' 
```
上述格式字符串中的 % s称为转换说明符，指出了要将值插入什么地方
```
>>> from string import Template
>>> tmpl = Template("Hello, $who! $what enough for ya?")
>>> tmpl.substitute(who="Mars", what = "Dusty")

'Hello, Mars! Dusty enough for ya?'
```
### format
编写新代码时，应选择使用字符串方法format，它融合并强化了早期方法的优点。使用这种
方法时，每个替换字段都用花括号括起，其中可能包含名称，还可能包含有关如何对相应的值进
行转换和格式设置的信息。  
• 在最简单的情况下，替换字段没有名称或将索引用作名称。
```
>>> "{}, {} and {}".format("first", "second", "third")
'first, second and third'
>>> "{0}, {1} and {2}".format("first", "second", "third")
'first, second and third' 
```
• 然而，索引无需像上面这样按顺序排列
```
>>> "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")
'to be or not to be'
```
• 命名字段的工作原理与你预期的完全相同。
```
>>> from math import pi
>>> "{name} is approximately {value:.2f}.".format(value=pi, name = "π")
'π is approximately 3.14.'
```

# 字符串方法

### 字符串的大小写
```python
name = "adalovelace"
print(name.title())  # AdaLovelace
print(name.upper())  # ADALOVELACE
print(name.lower())  # adalovelace
```
### 合并（拼接）字符串
```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + "" + last_name
print(full_name)  # adalovelace
print("Hello," + full_name.title() + "!")  # Hello,AdaLovelace!
```

### 制表符或换行符来添加空白
```python
print("Python")
  # Python
print("\tPython")
  #     Python
```
要在字符串中添加制表符，可使用字符组合\t
要在字符串中添加换行符，可使用字符组合\n
```python
print("Languages:\n\tPython\n\tC\n\tJavaScript")
```
```
Languages:
    Python
    C
    JavaScript
```


### 删除空白
```python
favorite_language = " python"
favorite_language.rstrip()     # 'python'
```
要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中
```python
favorite_language = 'python'
favorite_language = favorite_language.rstrip()
print(favorite_language)  # 'python'
```
你还可以剔除字符串开头的空白，或同时剔除字符串两端的空白。为此，可分别使用方法lstrip()
和strip()


### center
方法center通过在两边添加填充字符（默认为空格）让字符串居中。
```
>>> "The Middle by Jimmy Eat World".center(39)
'The Middle by Jimmy Eat World'
>>>"The Middle by Jimmy Eat World".center(39,"*")
'*****The Middle by Jimmy Eat World*****'
```


### Find
方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回 - 1。
```
>>> 'With a moo-moo here, and a moo-moo there'.find('moo')   # 7
>>> title = "Monty Python's Flying Circus"
>>> title.find('Monty')     # 0
>>> title.find('Python')    # 6
>>> title.find('Flying')    # 15
>>> title.find('Zirquss')   # -1 
```
你还可指定搜索的起点和终点（它们都是可选的）。
```
>>> subject = '$$$ Get rich now!!! $$$'
>>> subject.find('$$$')                                   # 0
>>> subject.find('$$$', 1)   #  只指定了起点                #20
>>> subject.find('!!!')                                   # 16
>>> subject.find('!!!', 0, 16)   #  同时指定了起点和终点     #-1
```

### join
join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素。
```python
seq=[1,2,3,4,5]
sep='+'
sep.join(seq) #  尝试合并一个数字列表
```
```
Traceback (most recent call last):
     File "<stdin>", line 1,  in  ?
TypeError: sequence item 0: expected string, int found
```
```python
seq=['1','2','3','4','5']
sep='+'
sep.join(seq)  #  合并一个字符串列表
'1+2+3+4+5'
```
```python
dirs='','usr','bin','env'
'/'.join(dirs) # '/usr/bin/env'
print('C:'+'\\'.join(dirs)) # C:\usr\bin\env
```

### Lower
方法lower返回字符串的小写版本。
```python
'Trondheim Hammer Dance'.lower()
'trondheim hammer dance'
```

### replace
方法replace将指定子串都替换为另一个字符串，并返回替换后的结果。
```python
'This is a test'.replace('is','eez')
'Theez eez a test'
'This is a test is'.replace('is', 'as')
'Thas as a test as'
```

### split
split是一个非常重要的字符串方法，其作用与join相反，用于将字符串拆分为序列。
```python
'1+2+3+4+5'.split('+')
# ['1','2','3','4','5']
'/usr/bin/env'.split('/')
# ['', 'usr', 'bin', 'env']
'Using the default'.split()
# ['Using', 'the', 'default']
```

### strip
方法strip将字符串开头和末尾的空白（但不包括中间的空白）删除，并返回删除后的结果。
```python
' internal whitespace is kept '.strip()
# 'internal whitespace is kept' 
```
你还可在一个字符串参数中指定要删除哪些字符。
```python
'*** SPAM * for * everyone!!! ***'.strip(' *!')
# 'SPAM * for * everyone'
```

### translate
方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
```python
# 使用translate前必须创建一个转换表
table = str.maketrans('cs', 'kz')
# 创建转换表后，就可将其用作方法translate的参数。
'this is an incredible test'.translate(table)
'thiz iz an inkredible tezt'
# 调用方法maketrans时，还可提供可选的第三个参数，指定要将哪些字母删除。
table = str.maketrans('cs', 'kz', ' ')
'this is an incredible test'.translate(table)
'thizizaninkredibletezt'
```

### 判断字符串是否满足特定的条件
isalnum、isalpha、isdecimal、isdigit、isidentifier、islower、isnumeric、 isprintable、isspace、istitle、isupper。

