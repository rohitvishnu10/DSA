class binarytree:
    class node:
        def __init__(self):
            self.value = 0
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = self.node()
        self.sz = 0
        self.ht = 0

    def buildtree(self, arr):
        nodelist = [None]
        for i in range(1, len(arr)):
            tempnode = self.node()
            tempnode.value = arr[i]
            if i != 1:
                tempnode.parent = nodelist[int(i / 2)]
                if i % 2 == 0:
                    tempnode.parent.left = tempnode
                else:
                    tempnode.parent.right = tempnode
            nodelist.append(tempnode)
        self.root = nodelist[1]
        self.sz = len(nodelist)
        return nodelist

    def printtree(self,nlist):
        for i in range(1,len(nlist)):
            print(nlist[i].value,end=" ")
        print(" ")

    def inorder(self,root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.value,end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value, end=" ")

    def preorder(self,root):
        if root is None:
            return
        print(root.value,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def findascendants(self,value,nlist):
        node=self.searchnode(value,nlist)
        while node.parent is not None:
            print(node.parent.value)
            node=node.parent


    def searchnode(self,value,nlist):
        for i in nlist[1::]:
            if value==i.value:
                return i

    def finddescendants(self,value,nlist):
        node=self.searchnode(value,nlist)
        self.postorder(node)









b1 = binarytree()
arr = list(map(int, input("Enter the tree elements: ").split()))
nlist = b1.buildtree(arr)
b1.printtree(nlist)
b1.inorder(b1.root)
print(" ")
b1.postorder(b1.root)
print(" ")
b1.preorder(b1.root)
print(" ")
# b1.findascendants(4,nlist)
b1.finddescendants(2,nlist)

