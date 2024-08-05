class activitystack:
    class nodes:
        def __init__(self,value):
            self.data=value
            self.next=None
    def __init__(self):
        self.head=self.nodes(None)
        self.sz=0

    def push(self,val):
        newnode=self.nodes(val)
        if self.sz==0:
            self.head=newnode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
        self.sz+=1

    def pop(self):
        if self.sz==0:
            print("no activities available",end=" ")
        elif self.sz==1:
            temp=self.head
            self.head=None
            self.sz-=1
            return temp.data
        else:
            temp=self.head
            while temp.next:
                prev=temp
                temp=temp.next
            prev.next=None
            self.sz-=1
            return temp.data


    def printactivities(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next




