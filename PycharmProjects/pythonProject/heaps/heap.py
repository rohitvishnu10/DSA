class Heap:
    def __init__(self):
        self.hp = []

    def swap(self, first, second):
        self.hp[first], self.hp[second] = self.hp[second], self.hp[first]

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def insert(self, val):
        self.hp.append(val)
        self.upheap(len(self.hp) - 1)

    def upheap(self, index):
        while index > 0:
            p = self.parent(index)
            if self.hp[index] < self.hp[p]:
                self.swap(index, p)
                index = p
            else:
                break

    def remove(self):
        if not self.hp:
            print("Heap is empty")
            return None
        temp = self.hp[0]
        last = self.hp.pop()
        if self.hp:
            self.hp[0] = last
            self.downheap(0)
        return temp

    def downheap(self, index):
        len_hp = len(self.hp)
        while True:
            left = self.left(index)
            right = self.right(index)
            smallest = index

            if left < len_hp and self.hp[left] < self.hp[smallest] :
                smallest = left
            if right < len_hp and self.hp[right] < self.hp[smallest]:
                smallest = right

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break

    def heapsort(self):
        sorted_list = []
        while self.hp:
            sorted_list.append(self.remove())
        return sorted_list

h = Heap()
h.insert(3)
h.insert(1)
h.insert(1)
h.insert(0)


print(h.heapsort())
