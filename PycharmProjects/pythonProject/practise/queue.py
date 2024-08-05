class queue:
    def __init__(self,size):
        self.size=size
        self.data=[None]*size
        self.front=0
        self.rear=-1
        self.sz=0

    def enqueue(self,val):
        if self.sz==self.size:
            print("queue is full")
        else:
            self.rear=(self.rear+1)%self.size
            self.data[self.rear]=val
            self.sz+=1

    def dequeue(self):
        if self.sz==0:
            print("queue is emptyy")
        else:
            element=self.data[self.front]
            self.data[self.front]=None
            self.front=(self.front+1)%self.size
            self.sz-=1
            return element


    def printqueue(self):
        if self.size==0:
            print("stack is empty")
        else:
            for i in self.data:
                if i != None:
                    print(i,end=" ")
q=queue(4)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(1)
q.dequeue()

q.printqueue()