from contentstack import *
class directory:
    class node:
        def __init__(self):
            self.name=""
            self.content=contents()
            self.deleted=contents()
            self.parent=None
            self.left=None
            self.right=None

    def __init__(self):
        self.root=self.node()
        self.sz=0
        self.ht=0

    def bilddirect(self,vlist):
        nodelist=[]
        nodelist.append(None)
        for i in range(1,len(vlist)):
            tempnode=self.node()
            tempnode.name=vlist[i]
            if i!=1:
                tempnode.parent=nodelist[int(i/2)]
                if i%2==0:
                    tempnode.parent.left=tempnode
                else:
                    tempnode.parent.right=tempnode
            nodelist.append(tempnode)
        self.root=nodelist[1]
        self.sz=len(nodelist)-1
        return nodelist

    def printnames(self,nodelist):
        for i in nodelist:
            if i!=None:
                print(i.name,end=" ")

    def searchdir(self,dirname,nlist):
        for i in nlist:
            if i.name==dirname:
                return i

    def addchild(self,node,dirname):
        newnode=self.node
        if node.left==None:


    def addsubdir(self,node,dirname,nlist):
        di=self.search(dirname,nlist)
        self.add
d=directory()
nlist=d.bilddirect(list((input("enter the tree names").split())))
d.printnames(nlist)


