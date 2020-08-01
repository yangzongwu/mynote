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

if __name__=='__main__':
    print(merge_sort([54,26,93,17,18,6,20]))