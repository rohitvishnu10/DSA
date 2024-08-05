class linkedl:
    class node:
        def __init__(self,val):
            self.data=val
            self.next=None
    def __init__(self):
        self.head=None
        self.size=0

    def addlast(self,val):
        newnode=self.node(val)
        if self.size==0:
            self.head=newnode
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.next=newnode
        self.size+=1

    def addfirst(self,val):
        newnode=self.node(val)
        if self.size==0:
            self.head=newnode
        else:
            temp=self.head
            newnode.next=temp
            self.head=newnode
        self.size+=1

    def deletefirst(self):
        if self.size==0:
            print("list is empty")
        elif self.size==1:
            self.head=None
            self.size-=1
        else:
            temp=self.head
            self.head=self.head.next
            del temp
            self.size-=1

    def deletelast(self):
        if self.size == 0:
            print("list is empty")
        elif self.size == 1:
            self.head = None
            self.size -= 1
        else:
            temp=self.head
            while(temp.next):
                prev=temp
                temp=temp.next
            temp=prev.next
            prev.next=None
            del(temp)
            self.size-=1

    def printlist(self):
        if self.size==0:
            print("list is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,end=" ")
                temp=temp.next

l=linkedl()
l.addlast(4)
l.addlast(5)
l.addlast(6)
l.addlast(7)
l.addfirst(1)
l.addfirst(2)
l.deletefirst()
l.deletefirst()
l.deletelast()
l.deletelast()
l.printlist()


    