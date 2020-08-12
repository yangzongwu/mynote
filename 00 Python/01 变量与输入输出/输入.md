函数input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便使用。
```python
message=input("Tell me something")
print(message)
```

函数input() 接受一个参数：  
即要向用户显示的提示 提示 或说明，让用户知道该如何做。在这个示例中，Python运行第1行代码时，用户将看到提示Tell me something。程序等待用户输入，并在用户按回车键后继续运行。输入存储在变量message 中，接下来的print(message) 将输入呈现给用户：
```python
name=input("Please enter your name: ")
print("Hello, "+name+"!")
```

有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。在这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input() 。这样，即便提示超过 一行，input() 语句也非常清晰。
```python
prompt="If you tell us who you are."
prompt+="\nWhat is your first name? "
name=input(prompt)
print("\nHello, "+name+"!")
```

使用int() 来获取数值输入，使用函数input() 时，Python将用户输入解读为字符串。请看下面让用户输入其年龄的解释器会话：
```python
age=input("How old are you? ")
# How old are you? 21
print(age)# '21'
age=int(age)# 21
```
