def insert_sort(alist):
    for i in range(1,len(alist)):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j-1],alist[j]=alist[j],alist[j-1]
            else:
                break
    print(alist)
    return alist

if __name__=='__main__':
    insert_sort([54,26,93,17,18,6,20])