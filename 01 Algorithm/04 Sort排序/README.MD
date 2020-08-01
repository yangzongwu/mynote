# 排序算法的稳定性
对如下数组第一个元素进行排序：  
(4,1),(3,1),(3,7),(5,6)  
* 维持次序(稳定)(3,1),(3,7),(4,1),(5,6)  
* 次序被改变(不稳定)(3,7),(3,1),(4,1),(5,6)  

# 冒泡排序
```
Fist pass
(54),(36), 93,  17
 36, (54),(93), 17
 36,  54, (93),(17)
 36,  54,  17,  93-->n-1不定，最后一位93固定
second pass
(36),(54), 17,  93
 36, (54),(17), 93
 36,  17,  54,  93-->n-2不定，最后两位54，93固定
third pass
(36),(17), 54, 93
 17,  36,  54, 93
```
```python
def bubble_sort(alist):
    for k in range(len(alist)-1,0,-1):
        for i in range(k):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
    return alist
```
### 时间复杂度
* 最优时间复杂度：n*n?[1，2，3，4，5]
* 最差时间复杂度：n*n
* 稳定

### 优化
最优时间复杂度：n  
```python
def bubble_sort(alist):
    for k in range(len(alist)-1,0,-1):
        flag=False
        for i in range(k):
            if alist[i]>alist[i+1]:
                flag=True
                alist[i],alist[i+1]=alist[i+1],alist[i]
        if flag==False:
            break
    return alist
```
# 选择排序
```
54，36，93，17----93最大
54，36，17，93----54最大
17，36，54，93----36最大
17，36，54，93----17 last one
```
```python
def select_sort(alist):
    for k in range(len(alist)-1,0,-1):
        n=len(alist)
        for j in range(n-1):
            min_index=j
            for i in range(j+1,n):
                if alist[min_index]>alist[i]:
                    min_index=i
            alist[j],alist[min_index]=alist[min_index],alist[j]
```
### 时间复杂度
* 最优时间复杂度：n*n
* 最差时间复杂度：n*n
* 不稳定 [1,26,26] 考虑升序最大第一个26会先选择，两个26位置交换

# 插入算法
```
54，         36，93，17
36,54        93,17
36,54,93     17
17,36,54,93  ---OK
```
```python
def insert_sort(alist):
    for i in range(1,len(alist)):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j-1],alist[j]=alist[j],alist[j-1]
            else:
                break
    return alist
```
### 时间复杂度
* 最优时间复杂度：n
* 最差时间复杂度：n*n
* 稳定

# 快速排序
```
(54) 26 93 17 77 31 44 55 20
-->low 26-->low 93 比54大
-->high 20 比54小
交换
（54）26 20 17 77 31 44 55 93
-->low 20-->low 17-->low 77
-->high 93-->high 55-->high 44 
交换
（54）26 20 17 44 31 77 55 93
-->low 31-->low==high
26 20 17 44 31 (54) 77 55 93
repeat: 26 20 17 44 31
repeat: 77 55 93
```
```python
def quick_sort(alist):
    if len(alist)<=1:
        return alist
    target=alist[0]
    l=1
    r=len(alist)-1
    while l<r:
        while l<r and alist[l]<=target:
            l+=1
        while r>l and alist[r]>=target:
            r-=1
        if r>l:
            alist[l],alist[r]=alist[r],alist[l]
            l+=1
            r-=1
        else:
            break
    if alist[l]>=target:
        res=quick_sort(alist[1:l])+[target]+quick_sort(alist[l:])
    else:
        res = quick_sort(alist[1:l+1]) + [target] + quick_sort(alist[l+1:])
    return res
```
### 时间复杂度
* 最优时间复杂度：O(n*logn)
* 最差时间复杂度：O(n**2)
* 不稳定

### 归并算法
```
54 26 93 17 77 31 44 55 
54 26 93 17  |   77 31 44 55 
54 26  | 93 17 |   77 31  |  44 55
54 | 26 |  93 |  17 |  77 |  31 |  44 |  55
26 54  |  17 93 |  31 77 |  44 55
17 26 54 93  |   31 44 55 77
17 26 31 44 54 55 77 93
```
```python
def merge_sort(alist):
    if len(alist)<=1:
        return alist

    k=len(alist)//2
    alist_left=merge_sort(alist[:k])
    alist_right=merge_sort(alist[k:])
    def mergeTwoList(l1,l2):
        rep=[]
        p1,p2=0,0
        while p1<len(l1) and p2<len(l2):
            if l1[p1]<=l2[p2]:
                rep.append(l1[p1])
                p1+=1
            else:
                rep.append(l2[p2])
                p2+=1
        rep+=l1[p1:]
        rep+=l2[p2:]
        return rep

    return mergeTwoList(alist_left,alist_right)
```
### 时间复杂度
* 最优时间复杂度：O(n*logn)
* 最差时间复杂度：O(n*logn)
* 稳定
* 有额外的开销，新的list存储