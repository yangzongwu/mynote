# stack
后进先出  
```python
class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)
```
#　queue
先进先出
```python
class Queue():
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0,item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)
```
双端队列
```python
class Dequeue():
    def __init__(self):
        self.dequeue = []

    def is_empty(self):
        return self.dequeue == []

    def enqueue_front(self, item):
        self.dequeue.insert(0,item)

    def enqueue_end(self, item):
        self.dequeue.append(item)

    def dequeue_end(self):
        return self.dequeue.pop()

    def dequeue_front(self):
        return self.dequeue.pop(0)

    def size(self):
        return len(self.dequeue)


```