Python标准库标准库是一组模块，安装的Python都包含它。  

你现在对类的工作原理已有大致的了解，可以开始使用其他程序员编写好的模块了。  
可使用标准库中的任何函数和类，为此只需在程序开头包含一条简单的import语句。  

下面来看模块collections中的一个类——OrderedDict。  
字典让你能够将信息关联起来，但它们不记录你添加键—值对的顺序。要创建字典并记录其中的键—值对的添加顺序，可使用模块collections中的OrderedDict类。OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。  


```python
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
```