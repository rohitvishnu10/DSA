from activitystack import *
class charlist:
    class node:
        def __init__(self,name):
            self.name=name
            self.next=None
            self.activities=activitystack()
            self.undo=activitystack()
            self.fc=0
            self.tc=0
            self.bc=0

    def __init__(self):
        self.head=self.node(None)
        self.size=0

    def createcharacter(self,name):
        newnode=self.node(name)
        if self.size==0:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
        self.size+=1

    def printcharacters(self):
        temp=self.head
        while temp:
            print(temp.name,end=" ")
            temp=temp.next

    def search(self,name):
        temp=self.head
        while temp:
            if temp.name==name:
                return temp
            temp=temp.next

    def doactivity(self,name,activityname):
        nod=self.search(name)
        if activityname=="f":
            nod.activities.push(activityname)
            nod.activities.printactivities()
            print(" ")
            nod.fc+=1
        elif activityname=="t":
            nod.activities.push(activityname)
            nod.activities.printactivities()
            print(" ")
            nod.tc+=1
        elif activityname=="b":
            nod.activities.push(activityname)
            nod.activities.printactivities()
            print(" ")
            nod.bc+=1
        elif activityname=="u":
            if nod.activities.sz==0:
                print("undo failed")
            else:
                nod.undo.push(nod.activities.pop())
                print("undo successfull")
                nod.undo.printactivities()

        elif activityname=="r":
            if nod.undo.sz==0:
                print("redo failed")
            else:
                nod.activities.push(nod.undo.pop())
                print("redo successfull")
                nod.activities.printactivities()



u1=charlist()
u1.createcharacter("pokemon")
u1.createcharacter("charmander")
u1.doactivity("pokemon","f")
u1.doactivity("pokemon","t")
u1.doactivity("pokemon","u")
u1.doactivity("pokemon","r")




