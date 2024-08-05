class sllist:
    class node:
        def __init__(self, data):
            self.element = data
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isempty(self):
        return self.size == 0
    
    def insertfirst(self, data):
        if self.size == 0:
            newnode = self.node(data)
            newnode.next = newnode  # Circular link
            self.head = newnode
            self.tail = newnode
        else:
            newnode = self.node(data)
            newnode.next = self.head
            self.tail.next = newnode
            self.head = newnode
        self.size += 1

    def printlist(self):
        if self.size == 0:
            print("empty")
        else:
            current = self.head
            while True:
                print(current.element, end=" ")
                current = current.next
                if current == self.head:
                    break
        print(" ")

    def insertlast(self, data):
        if self.size == 0:
            self.insertfirst(data)
        else:
            newnode = self.node(data)
            newnode.next = self.head
            self.tail.next = newnode
            self.tail = newnode
            self.size += 1

    def deletefirst(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.tail.next = self.head.next
            self.head = self.head.next
            self.size -= 1

    def deletelast(self):
        if self.size == 0:
            print("List is empty")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
            self.size -= 1

   

l = sllist()

l.insertfirst(90)
l.insertfirst(89)
l.insertfirst(50)
l.printlist()  # Output: 50 89 90
l.insertlast(70)
l.printlist()  # Output: 50 89 90 70

l.deletefirst()
l.printlist()  # Output: 89 90 70

l.deletelast()
l.printlist()  # Output: 89 90
