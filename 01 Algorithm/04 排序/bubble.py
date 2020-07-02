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

if __name__=='__main__':
    bubble_sort([54,26,93,17,18,6,20])