# import
从模块导入时，通常使用  
```py
import somemodule 
```
或使用
```py
from somemodule import somefunction  
```
或  
```py
from somemodule import somefunction, anotherfunction, yetanotherfunction  
```
或 
```py
from somemodule import *   
```
如果有重复的？--别名  
```py
>>> import math as foobar
>>> foobar.sqrt(4)
2.0 
>>> from math import sqrt as foobar
>>> foobar(4)
2.0 
from module1 import open as open1
from module2 import open as open2 
```