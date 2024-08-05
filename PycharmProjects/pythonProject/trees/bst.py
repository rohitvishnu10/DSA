class bst:
    class node:
        def __init__(self,val):
            self.data=val
            self.right=None
            self.left=None
            self.height=0

    def __init__(self):
        self.root=None

    def insert(self,val):
        self.root=self.insertval(self.root,val)

    def height(self,node):
        if node is None:
            return -1
        return node.height

    def insertval(self,node,val):
        if node is None:
            newnode=self.node(val)
            return newnode
        if node.data < val:
            node.left=self.insertval(node.left,val)

        elif node.data>val:
            node.right=self.insertval(node.right,val)
        else:
            return node

        node.height=max(self.height(node.left),self.height(node.right))+1
        return node

    def checkbalanced(self):
        ans=self.balanced(self.root)
        return ans

    def balanced(self,node):
        if node is None:
            return True
        left=self.height(node.left)
        right=self.height(node.right)

        if abs(left-right) >1:
            return False
        return self.balanced(node.left) and self.balanced(node.right)

tree = bst()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(12)
tree.insert(18)
print(tree.checkbalanced())

