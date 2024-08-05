class bt:
    class node:
        def __init__(self,val):
            self.data=val
            self.left=None
            self.right=None
            self.parent=None
    def __init__(self):
        self.sz=0
        self.root=None

    def addchild(self,parent,child,first):
        if self.root is None:
            self.root=self.node(parent)
            self.sz=1
        node=self.findnode(self.root,parent)
        if node is None:
            print("parent is not found")
            return
        child=self.node(child)
        if first:
            if node.left is None:
                node.left=child
            else:
                print("el already exists")
        else:
            if node.right is None:
                node.right=child
            else:
                print("el already exists")
        child.parent=node
        self.sz+=1

    def findnode(self,root,element):
        if root is None:
            return None
        if root.element==element:
            return root
        left=self.findnode(root.left,element)
        if left is not None:
            return left
        right=self.findnode(root.right,element)
        return right

    def heightf(self,node):
        fn=self.findnode(self.root,node)
        if fn is None:
            return
        return self.heightf(fn)

    def height(self,node):
        if node is None:
            return -1
        lefth=self.heightf(node.left)
        righth=self.heightf(node.right)
        return max(lefth,righth)



