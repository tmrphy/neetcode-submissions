class Deque:

    class Node:

        def __init__(self, data = None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev
            
    
    def __init__(self):
        
        self.head = Deque.Node()
        self.tail = Deque.Node()
        self.size = 0
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        left, right = self.tail.prev, self.tail
        new_node = Deque.Node(value, next = right, prev = left)
        left.next = new_node
        right.prev = new_node
        self.size += 1

    def appendleft(self, value: int) -> None:
        left, right = self.head, self.head.next
        new_node = Deque.Node(value, next = right, prev = left)
        left.next = new_node
        right.prev = new_node
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        node = self.tail.prev
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        self.size -= 1
        return node.data

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        node = self.head.next
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        self.size -= 1
        return node.data
