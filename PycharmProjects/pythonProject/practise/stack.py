class stack:
    def __init__(self,size):
        self.data=[None]*size
        self.size=size
        self.top=-1

    def push(self,val):
        if self.top==self.size-1:
            print("stack is full")
        else:
            self.top+=1
            self.data[self.top]=val

    def pop(self):
        if self.top==-1:
            print("stack is empty")
        else:
            element=self.data[self.top]
            self.data[self.top]=None
            self.top-=1
            return element

    def printstack(self):
        while self.top>=0:
            print(self.pop())


s=stack(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.printstack()


