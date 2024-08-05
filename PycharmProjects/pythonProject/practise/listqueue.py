
from slist import sllist  

class Queue:
    def __init__(self):
        self.items = sllist()

    def isempty(self):
        return self.items.isempty()

    def enqueue(self, data):
        self.items.insertlast(data)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return None
        else:
            front_element = self.items.head.element
            self.items.deletefirst()
            return front_element

    def front(self):
        if self.isempty():
            print("Queue is empty")
            return None
        else:
            return self.items.head.element
        
    def printqueue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            current = self.items.head
            while current:
                print(current.element, end=" ")
                current = current.next
            print("")



queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.front())  

print("Dequeued element:", queue.dequeue())  
print("Dequeued element:", queue.dequeue())  
print("Front element after dequeue:", queue.front())  
