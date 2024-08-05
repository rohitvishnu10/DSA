
from slist import sllist  
class Stack:
    def __init__(self):
        self.items = sllist()

    def isempty(self):
        return self.items.isempty()

    def push(self, data):
        self.items.insertfirst(data)

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        else:
            top_element = self.items.head.element
            self.items.deletefirst()
            return top_element

    def peek(self):
        if self.isempty():
            print("Stack is empty")
            return None
        else:
            return self.items.head.element


# Testing the stack implementation
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek()) 

print("Popped element:", stack.pop())  
print("Popped element:", stack.pop()) 

print("Top element after pops:", stack.peek())  
