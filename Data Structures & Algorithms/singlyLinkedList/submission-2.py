class LinkedList:
    
    class Node:

        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next_node = next_node
             

    def __init__(self):
        self.head = LinkedList.Node()
        self.node_count = 0

    def __iter__(self):
        curr_node = self.head.next_node
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next_node
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.node_count:
            return -1
        curr_node = self.head.next_node
        for _ in range(index):
            curr_node = curr_node.next_node
        return curr_node.data 

    def insertHead(self, val: int) -> None:
        self.head.next_node = LinkedList.Node(val, self.head.next_node)
        self.node_count += 1

    def insertTail(self, val: int) -> None:
        curr_node = self.head
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node
        curr_node.next_node = LinkedList.Node(val)
        self.node_count += 1

    def remove(self, index: int) -> bool:

        if index < 0 or index >= self.node_count:
            return False
        
        curr_node = self.head.next_node
        prev_node = self.head
        for _ in range(index):
            prev_node = curr_node
            curr_node = curr_node.next_node
        
        prev_node.next_node = curr_node.next_node
        self.node_count -= 1
        return True

    def getValues(self) -> List[int]:
        return list(self)
