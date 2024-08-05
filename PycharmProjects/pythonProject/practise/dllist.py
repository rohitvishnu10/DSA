class dllist:
    class node:
        def __init__(self, data):
            self.element = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = self.node(None)
        self.tail = self.head
        self.size = 0

    def isempty(self):
        return self.size == 0

    def insertfirst(self, data):
        if self.size == 0:
            self.head = self.node(data)
            self.tail = self.head
        else:
            newnode = self.node(data)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.size += 1

    def deletefirst(self):
        if self.size == 0:
            print("empty")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
            self.size -= 1

    def insertlast(self, data):
        if self.size == 0:
            self.head = self.node(data)
            self.tail = self.head
        else:
            newnode = self.node(data)
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.size += 1

    def deletelast(self):
        if self.size == 0:
            print("empty")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del temp
            self.size -= 1

    def printlist(self):
        if self.size == 0:
            print("empty")
        else:
            current = self.head
            while current != None:
                print(current.element, end=" ")
                current = current.next
        print(" ")

# Example usage:
l = dllist()
l.insertfirst(9)
l.insertfirst(8)
l.printlist()
l.insertlast(7)
l.insertlast(9)
l.printlist()
l.deletefirst()
l.deletelast()
l.printlist()
