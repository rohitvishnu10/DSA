class doubly:
    class node:
        def __init__(self,value):
            self.data=value
            self.left=None
            self.right=None

    def __init__(self):
        self.head=self.node(None)
        self.tail=self.head
        self.size=0

    def addfirst(self,val):
        newnode=self.node(val)
        if self.size==0:
            self.head=newnode
            self.head.right=self.head
            self.head.left=self.head
            self.tail=self.head
        elif self.size==1:
            newnode.right=self.head
            self.tail=newnode.right
            self.head.left=newnode
            self.head=newnode
            self.tail.left=self.head
            newnode.left=self.tail
        else:
            newnode.right=self.head
            self.head.left=newnode
            self.head=newnode
        self.size+=1

    def addlast(self,val):
        newnode=self.node(val)
        if self.size==0:
            self.head=newnode
            self.head.right=self.head
            self.head.left=self.head
            self.tail=self.head
        else:
            newnode.left=self.tail
            self.tail.right=newnode
            newnode.right=self.head
            self.tail=newnode
        self.size+=1

    def printdoubly(self):
        if self.size==0:
            print("list is empty")
        else:
            temp=self.head
            while temp!=self.tail:
                print(temp.data,end=" ")
                temp=temp.right
            print(temp.data)

    def printreverse(self):
        if self.size==0:
            print("list is empty")
        else:
            temp=self.tail
            while temp!=self.head:
                print(temp.data, end=" ")
                temp = temp.left
            print(temp.data)

    def deletefirst(self):
        if self.size==0:
            print("list is empty")
        elif self.size==1:
            self.head=None
            self.tail=None
            self.size-=1
        else:
            ans=self.head
            next=self.head.right
            next.left=self.tail
            self.head=next
            del(ans)
            self.size -= 1
    def deletelast(self):
        if self.size==0:
            print("list is empty")
        elif self.size==1:
            self.head=None
            self.tail=None
            self.size -= 1
        else:
            ans=self.tail
            prev=self.tail.left
            prev.right=self.head
            self.tail=prev
            del ans
            self.size -= 1






d=doubly()
d.addfirst(5)
d.addfirst(6)
d.addfirst(7)
d.addlast(8)
d.deletefirst()
d.deletelast()
d.printdoubly()
d.printreverse()
