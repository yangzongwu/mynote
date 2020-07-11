# 概述
* 每个节点有零个或多个子节点；
* 没有父节点的节点称为根节点；
* 每一个非根节点有且只有一个父节点；
* 除了根节点，每个子节点可以分为多个不相交的子树；
### 树的术语  
* 节点的度： 一个节点的子树的个数；
* 树的度：最大的节点的度；
* 叶节点或终端节点：度为零的节点；
* 父节点：
* 子节点：
* 兄弟节点：
* 节点的层次：从根开始定义，根为第1层，根的子节点为第二层；
* 树的高度或者深度：树中节点的最大层次；
* 堂兄弟节点：父亲点在同一层的节点；
* 节点的祖先：从根到该节点所经分支上的所有节点；
* 子孙：以某节点为根的子树中任一节点是
* 深林： 由m(m>0)颗互相不相交的树的集合

### 树的种类  
* 无序树
* 有序树
    * 二叉树（节点的度最多只能是2）
        * 完全二叉树（n-1 层是满二叉树,最后一层最后一个节点前面都挂满了节点）
        * 满二叉树（每一层都挂满了节点）
        * 平衡二叉树(AVL树)：任意两科子树高度差不超过1
        * 排序二叉树(Binary Search Tree):树的节点是有序的
    * 霍夫曼树
    * B树

###　树的存储
* 顺序存储
* 链式存储


# 二叉树
二叉树性质编辑
* 性质1：二叉树的第i层上至多有2^(i-1)（i≥1）个节点
* 性质2：深度为h的二叉树中至多含有2^h-1个节点
* 性质3：若在任意一棵二叉树中，有n个叶子节点，有n2个度为2的节点，则必有n0=n2+1
* 性质4：具有n个节点的完全二叉树深为log2(x+1)（其中x表示不大于n的最大整数）
* 性质5：若对一棵有n个节点的完全二叉树进行顺序编号（1≤i≤n），那么，对于编号为i（i≥1）的节点:
    * 当i=1时，该节点为根，它无双亲节点
    * 当i>1时，该节点的双亲节点的编号为i/2
    * 若2i≤n，则有编号为2的左孩子，否则没有左孩子
    * 若2+1≤n，则有编号为2i+1的右孩子，否则没有右孩子
    

# 实现树与遍历
```python
class Node(object):
    def __init__(self,item):
        self.val=item
        self.lchild=None
        self.rchild=None

class Tree(object):
    def __init__(self):
        self.root=None

    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
            return

        queue=[self.root]
        while queue:
            cur_node=queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild=node
                return
            else:
                queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild=node
                    return
                else:
                    queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        rep=[]
        if self.root is None:
            return
        queue=[self.root]
        while queue:
            cur_node=queue.pop(0)
            rep.append(cur_node.val)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
        print("广度遍历",rep)

    def preOrder(self):
        """先序遍历"""
        rep=[]

        def dfs(root,rep):
            if not root:
                return
            rep.append(root.val)
            dfs(root.lchild,rep)
            dfs(root.rchild,rep)
        dfs(self.root,rep)
        print("先序遍历",rep)

    def inOrder(self):
        """中序遍历"""
        rep = []

        def dfs(root, rep):
            if not root:
                return
            dfs(root.lchild, rep)
            rep.append(root.val)
            dfs(root.rchild, rep)

        dfs(self.root, rep)
        print("中序遍历", rep)

    def postOrder(self):
        """后序遍历"""
        rep = []

        def dfs(root, rep):
            if not root:
                return
            dfs(root.lchild, rep)
            dfs(root.rchild, rep)
            rep.append(root.val)


        dfs(self.root, rep)
        print("后序遍历", rep)
if __name__=='__main__':
    tree=Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.breadth_travel()
    tree.preOrder()
    tree.inOrder()
    tree.postOrder()
```

### 反推树
* 给出中序遍历和先序遍历 求后序遍历
* 给出中序遍历和后序遍历 求先序遍历
