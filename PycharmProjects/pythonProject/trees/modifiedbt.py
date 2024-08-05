class mbt:
    class node:
        def __init__(self):
            self.name=""
            self.right=None
            self.left=None
            self.parent=None
    def __init__(self):
        self.root=self.node()
        self.ht=0
        self.size=0

    def findnode(self,nodename,curnode):
        if curnode is None:
            return None
        left=self.findnode(nodename,curnode.left)
        if left:
            return left
        if curnode.name==nodename:
            return curnode
        right=self.findnode(nodename,curnode.right)
        return right

    def addchild(self,nodename,childname,opt):
        node=self.findnode(nodename,self.root)
        if node is None:
            print("is not found")
            return
        newnode=self.node()
        newnode.name=childname
        newnode.parent=node
        if opt=='l':
            node.left=newnode
        else:
            node.right=newnode

    def isexternal(self,node):
        if node.left==None and node.right==None:
            return True
        else:
            False

    def levelorder(self):
        if self.root==None:
            print("is empy")
            return
        queue=[self.root]
        level=1
        while queue:
            print(level,"gen",end=" ")
            levelsz=len(queue)
            for i in range(levelsz):
                node=queue.pop(0)
                print(node.name,end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(" ")
            level+=1

    def getascendants(self,nodelement):
        node=self.findnode(nodelement,self.root)
        if node is None:
            print("empty")
            return
        asc=[]
        while node.parent:
            asc.append(node.parent.name)
            node=node.parent
        print(asc)


    def descend(self,nodelement):
        node=self.findnode(nodelement,self.root)
        if node is None:
            print("node empty")
            return
        desc=[]
        self.ded(node,desc)
        print(desc)

    def ded(self,node,desc):
        if node is None:
            return
        if node.left:
            desc.append(node.left.name)
            self.ded(node.left,desc)
        if node.right:
            desc.append(node.right.name)
            self.ded(node.right,desc)

    def depthofnode(self,nodelement):
        node=self.findnode(nodelement,self.root)
        if node is None:
            print("empty")
            return
        depth=self.depth(node)
        print(depth)

    def depth(self,node):
        if node.parent is None:
            return 0
        return 1+self.depth(node.parent)

    def insertafter(self,nodelement,newval,left):
        node=self.findnode(nodelement,self.root)
        if node is None:
            print("not found")
            return
        newnode=self.node()
        newnode.name=newval
        newnode.parent=node
        if self.isexternal(node)==True:
            if left:
                node.left=newnode
            else:
                node.right=newnode
        else:
            if left:
                l=node.left
                node.left=newnode
                l.parent=newnode
                newnode.left=l
            else:
                r=node.right
                node.right=newnode
                r.parent=newnode
                newnode.right=r

    def height(self,nodeelement):
        node=self.findnode(nodeelement,self.root)

        def maxl(v):
            if v is None:
                return 0
            if self.isexternal(v):
                return 0
            else:
                return 1+maxl(v.left)
        def maxr(v):
            if v is None:
                return 0
            if self.isexternal(v):
                return 0
            else:
                return 1+maxr(v.right)
        lh=maxl(node)
        rh=maxr(node)
        m=max(lh,rh)
        print(m)







m1=mbt()
m1.root.name="Sree"
m1.addchild("Sree","Rajesh","l")
m1.addchild("Sree","Sujesh","r")
m1.levelorder()
m1.getascendants("Rajesh")
m1.descend("Sree")
m1.depthofnode("Rajesh")
m1.height("Sree")