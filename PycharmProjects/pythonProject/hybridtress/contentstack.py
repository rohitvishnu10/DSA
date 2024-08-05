class contents:
    class node:
        def __init__(self,value):
            self.data=value
            self.next=None
    def __init__(self):
        self.head=self.node(None)
        self.size=0

    def push(self,val):
        newnode=self.node(val)
        if self.size==0:
            self.head=newnode
            print("pushed file name " + str(val))
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
            print("pushed file name "+str(val))
        self.size+=1

    def printcontents(self):
        temp=self.head
        print("contents in directory is ",end=" ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print(" ")

    def pop(self):
        if self.size==0:
            print("the contents are none in this")
        elif self.size==1:
            temp=self.head
            self.head=None
            self.size-=1
            return temp.data
        else:
            temp=self.head
            while temp.next:
                prev=temp
                temp=temp.next
            prev.next=None
            self.size-=1
            return temp.data



c=contents()
c.push(5)
c.push(6)
c.printcontents()
print(c.pop())