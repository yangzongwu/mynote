 # 单项链表
 ```python
class SingleNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList(object):
    def __init__(self, node=None):
        self.head = None

    def is_empty(self):
        return self.head == None

    def length(self):
        p = self.head
        cnt = 0
        while p:
            cnt += 1
            p = p.next
        return cnt

    def travel(self):
        rep = []
        p = self.head
        while p:
            rep.append(p.val)
            p = p.next
        return rep

    def add_front(self, item):
        cur = self.head
        newhead = SingleNode(item)
        newhead.next = cur
        self.head = newhead

    def append(self, item):
        node = SingleNode(item)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        node = SingleNode(0)
        node.next = self.head
        p = node
        while pos > 0:
            p = p.next
            pos -= 1
        next_link = p.next
        new_node = SingleNode(item)
        new_node.next = next_link
        p.next = new_node
        return node.next

    def remove(self, item):
        node=SingleNode(0)
        node.next=self.head
        p=node
        while p.next:
            if p.next.val==item:
                p.next=p.next.next
                break
            else:
                p=p.next
        return node.next

    def search(self, item):
        p = self.head
        while p:
            if p.val == item:
                return True
            else:
                p = p.next
        return False

```

# 链表与顺序表
链表/顺序表，
* 访问元素 O(n) O(1)
* 在头部插入/删除 O(1) O(n)
* 在尾部插入/删除 O(n) O(1)
* 在中间插入/删除 O(n) O(n)
优缺点：
* 内存是分散的，顺序表内存是连续的  
* 需要额外的空间储存指针
* 访问元素变长

# 单项循环链表
```python
class SingleNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList(object):
    def __init__(self, node=None):
        self.head = node
        if node:
            node.next=node

    def is_empty(self):
        return self.head == None

    def length(self):
        if not self.head:
            return 0
        p = self.head
        cnt = 1
        while p.next!=self.head:
            cnt += 1
            p = p.next
        return cnt

    def travel(self):
        if not self.head:
            return []
        rep = []
        p = self.head
        while p.next!=self.head:
            rep.append(p.val)
            p = p.next
        rep.append(p.val)
        return rep

    def add_front(self, item):
        pass

    def append(self, item):
        pass

    def insert(self, pos, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass

```

# 双向链表
```python
class DoubleNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self,node=None):
        self._head = node

    def is_empty(self):
        return self._head is None

    def length(self):
        p = self._head
        cnt = 1
        while p:
            cnt += 1
            p = p.next
        return cnt

    def travel(self):
        rep = []
        p = self._head
        while p:
            rep.append(p.val)
            p = p.next
        return rep

    def add_front(self, item):
        cur = self._head
        newhead = DoubleNode(item)
        newhead.next = cur
        cur.prev=newhead
        self._head = newhead

    def append(self, item):
        node = DoubleNode(item)
        if not self._head:
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev=cur

    def insert(self, pos, item):
        node = DoubleNode(0)
        node.next = self._head
        p = node
        while pos > 0:
            p = p.next
            pos -= 1
        next_link = p.next
        new_node = DoubleNode(item)
        new_node.next = next_link
        p.next = new_node
        next_link.prev=new_node
        new_node.prev=p
        return node.next

    def remove(self, item):
        pass

    def search(self, item):
        p = self._head
        while p:
            if p.val == item:
                return True
            else:
                p = p.next
        return False
```