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
    if alist[l]>target:
        res=quick_sort(alist[1:l])+[target]+quick_sort(alist[l:])
    else:
        res = quick_sort(alist[1:l+1]) + [target] + quick_sort(alist[l+1:])
    return res

if __name__=='__main__':
    print(quick_sort([1,2,4,3,5,7,8,12,32,100,54,11]))