class BST:
    class Node:
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None
            self.height = 0

    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insertval(self.root, val)

    def height(self, node):
        if node is None:
            return -1
        return node.height

    def _insertval(self, node, val):
        if node is None:
            return self.Node(val)

        if val < node.data:
            node.left = self._insertval(node.left, val)
        elif val > node.data:
            node.right = self._insertval(node.right, val)
        else:

            return node

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self._rotate(node)

    def _rightrotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def _leftrotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    def _rotate(self, node):
        balance = self.height(node.left) - self.height(node.right)


        if balance > 1:
            if self.height(node.left.left) >= self.height(node.left.right):
                return self._rightrotate(node)
            else:
                node.left = self._leftrotate(node.left)
                return self._rightrotate(node)


        if balance < -1:
            if self.height(node.right.right) >= self.height(node.right.left):
                return self._leftrotate(node)
            else:
                node.right = self._rightrotate(node.right)
                return self._leftrotate(node)

        return node

    def checkbalanced(self):
        return self._balanced(self.root)

    def _balanced(self, node):
        if node is None:
            return True
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return self._balanced(node.left) and self._balanced(node.right)


t = BST()
for i in range(1000):
    t.insert(i)
print(t.root.height)
