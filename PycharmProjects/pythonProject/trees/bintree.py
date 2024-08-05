class tree:
    class node:
        def __init__(self):
            self.data = 0
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = self.node()
        self.sz = 0
        self.ht = 0

    def buldtree(self, arr):
        nodelist = []
        nodelist.append(None)
        for i in range(1, len(arr)):
            if arr[i] != -1:
                tempnode = self.node()
                tempnode.data = arr[i]
                if i != 1:
                    tempnode.parent = nodelist[int(i/2)]
                    if i % 2 == 0:
                        tempnode.parent.left = tempnode
                    else:
                        tempnode.parent.right = tempnode
                nodelist.append(tempnode)
            else:
                nodelist.append(None)
        self.root=nodelist[1]


    def printexpression(self, v):
        if v is not None:
            if self.is_external(v):
                print(v.data, end=" ")
            else:
                print("(", end=" ")
                self.printexpression(v.left)
                print(v.data, end=" ")
                self.printexpression(v.right)
                print(")", end=" ")

    def is_external(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def evaluate(self, node):
        if node is None:
            return 0
        if self.is_external(node):
            if node.data.isdigit():  # Check if the data is a number
                return int(node.data)
            else:
                return None  # Return None for operator nodes
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        operator = node.data
        if operator == '+':
            if left is not None and right is not None:
                return left + right
        elif operator == '-':
            if left is not None and right is not None:
                return left - right
        elif operator == '*':
            if left is not None and right is not None:
                return left * right
        elif operator == '/':
            if left is not None and right is not None:
                if right != 0:
                    return left / right
                else:
                    raise ValueError("Division by zero error")
        return None  # Return None if any operand is None


arr = list(input("enter elements").split())
t = tree()
t.buldtree(arr)


t.printexpression(t.root)
print()
print(t.evaluate(t.root))
