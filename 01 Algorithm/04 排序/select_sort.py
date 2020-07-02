def select_sort(alist):
    for k in range(len(alist)-1,0,-1):
        n=len(alist)
        for j in range(n-1):
            min_index=j
            for i in range(j+1,n):
                if alist[min_index]>alist[i]:
                    min_index=i
            alist[j],alist[min_index]=alist[min_index],alist[j]
    print(alist)
if __name__=='__main__':
    select_sort([1,34,53,12,45,2])