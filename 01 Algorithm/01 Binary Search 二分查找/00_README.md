# 适用范围
有序的序列  
[1,2,3,5,6,8,12]  

# 二分查找　
### 递归
```python
def binanry_search1(alist, item):
    """二分查找"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binanry_search1(alist[:mid], item)
        else:
            return binanry_search1(alist[mid + 1:], item)
    return False
if __name__ == "__main__":
    li = [1, 3, 5, 6, 7, 9, 12, 14, 16]
    print(binanry_search1(li, 55))
    print(binanry_search1(li, 5))
```
　
###　非递归
```python
def binanry_search2(alist, item):
    """二分查找 非递归"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False
```

# 时间复杂度
* 最优时间复杂度：O(1)
* 最坏时间复杂度：O(logn)