class sllist:
    class node:
        def __init__(self,data):
            self.element=data
            self.next=None
    
    def __init__(self):
        self.head=self.node(None)
        self.size=0

    def isempty(self):
        return self.size==0
    
    def insertfirst(self,data):
        if self.size==0:
            self.head.element=data
        else:
            newnode=self.node(data)
            newnode.next=self.head
            self.head=newnode
        self.size+=1

    def deletefirst(self):
        if self.size==0:
            print("empty")
        elif self.size==1:
            self.head.element=None
            self.size-=1
        else:
            temp=self.head
            self.head=self.head.next
            del temp
            self.size-=1

    def insertlast(self,data):
        if self.size==0:
            self.head.element=data
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            newnode=self.node(data)
            current.next=newnode
        self.size+=1

    def deletelast(self):
        if self.size==0:
            print("empty")
        elif self.size==1:
            self.head.element=None

        else:
            current=self.head
            while(current.next!=None):
                temp=current
                current=current.next
            
            temp.next=None
            del current
        self.size-=1

    def printlist(self):
        if self.size==0:
            print("empty")
        else:
            current=self.head
            while(current!=None):
                print(current.element,end=" ")
                current=current.next
        print(" ")

    def mid(self):
        if self.size==0:
            print("empty")
        else:
            
            n=self.size
            c=0
            current=self.head
            while(current.next!=None):
                c+=1
                if(c==n//2):
                    print("mid:",current.next.element)
                    break
                current=current.next

    
l=sllist()
l.insertfirst(9)
l.insertfirst(8)
l.printlist()
l.insertlast(7)


l.printlist()

l.mid()