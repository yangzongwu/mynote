# print
打印多个参数  
print可用于打印一个表达式，这个表达式要么是字符串，要么将自动转换为字符
串。但实际上，你可同时打印多个表达式，条件是用逗号分隔它们  
```py
>>> print('Age:', 42)
Age: 42 
```
```py
>>> name = 'Gumby'
>>> salutation = 'Mr.'
>>> greeting = 'Hello,'
>>> print(greeting, salutation, name)
Hello, Mr. Gumby
```
如果字符串变量greeting不包含逗号，如何在结果中添加呢？你不能像下面这样做：  
```py
print(greeting, ',', salutation, name)
```
因为这将在逗号前添加一个空格。下面是一种可行的解决方案：  
```py
print(greeting + ',', salutation, name)
```
它将逗号和变量greeting相加。如果需要，可自定义分隔符：  
```py
>>> print("I", "wish", "to", "register", "a", "complaint", sep="_")
I_wish_to_register_a_complaint
```
你还可自定义结束字符串，以替换默认的换行符。例如，如果将结束字符串指定为空字符串，
以后就可继续打印到当前行。  
```
print('Hello,', end='')
print('world!')
```