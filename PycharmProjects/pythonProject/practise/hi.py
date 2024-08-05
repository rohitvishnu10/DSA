class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0

    def getChildren(self, curnode):
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return (True)
        else:
            return (False)

    def isRoot(self, curnode):
        if (curnode.parent == None):
            return True
        else:
            return False

    def inorderTraverse(self, v):
        if self.isExternal(v):
            print(v.element, end=" ")

        else:
            self.inorderTraverse(v.leftchild)
            print(v.element, end=" ")
            self.inorderTraverse(v.rightchild)

    def preorderTraverse(self, v):
        if self.isExternal(v):
            print(v.element, end=" ")

        else:
            print(v.element, end=" ")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)

    def postorderTraverse(self, v):
        if self.isExternal(v):
            print(v.element, end=" ")

        else:
            self.postorderTraverse(v.leftchild)
            self.postorderTraverse(v.rightchild)
            print(v.element, end=" ")

    def delLeaves(self, v):
        if self.isExternal(v):
            v.parent.leftchild = None
            v.parent.rightchild = None
        else:
            self.delLeaves(v.leftchild)
            self.delLeaves(v.rightchild)

    def levelorderTraverse(self, v):
        print(nlist)

    def findDepth(self, v):
        if self.isRoot(v):
            return 0
        else:
            return 1 + self.findDepth(v.parent)

    def findHeight(self, v):
        def findmaxl(v):
            if self.isExternal(v):
                return 1
            else:
                return 1 + findmaxl(v.leftchild)

        def findmaxr(v):
            if self.isExternal(v):
                return 1
            else:
                return 1 + findmaxr(v.rightchild)

        lh = findmaxl(v)
        rh = findmaxr(v)
        return max(lh, rh)

    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[int(i / 2)]
                        if (i % 2 == 0):
                            nodelist[int(i / 2)].leftchild = tempnode
                        else:
                            nodelist[int(i / 2)].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz = len(nodelist)
        return nodelist

    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element, end=" ");
            else:
                print(None)

    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz


def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    nlist = tree.buildTree(arr)
    inputs = int(input())
    while inputs > 0:
        command = input()
        operation = command.split()
        if (operation[0] == "I"):
            tree.inorderTraverse(tree.root)
            print()
        elif (operation[0] == "P"):
            tree.preorderTraverse(tree.root)
            print()
        elif (operation[0] == "Post"):
            tree.postorderTraverse(tree.root)
            print()
        elif (operation[0] == "L"):
            tree.levelorderTraverse(tree.root)
            print()
        elif (operation[0] == "D"):
            pos = int(operation[1])
            print(tree.findDepth(nlist[pos]))
        elif (operation[0] == "H"):
            pos = int(operation[1])
            print(tree.findHeight(nlist[pos]))
        elif (operation[0] == "IP"):
            print(tree.isProper(tree.root))
        elif (operation[0] == 'M'):
            tree.mirror(tree.root)
            tree.levelorderTraverse(tree.root)
            print()
        elif (operation[0] == 'DL'):
            tree.delLeaves(tree.root)
            tree.levelorderTraverse(tree.root)
            print()
        elif (operation[0] == 'RL'):
            tree.root2leafsum(int(operation[1]))
            print()
        elif (operation[0] == 'ML'):
            tree.leastleaf()
            print()
        inputs -= 1


if __name__ == '__main__':
    main()
