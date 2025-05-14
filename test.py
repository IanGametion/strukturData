class Node:
    def __init__(self, data=None, next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next != None
    def set_prev(self, prev):
        self.prev = prev
    def get_prev(self):
        return self.prev
    def has_prev(self):
        return self.prev != None
    def __str__(self):
        return "Node[Data-%s]" % (self.data,)

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def misterius1(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def misterius2(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = NewNode
        NewNode.prev = last

dll = DoublyLinkedList()
dll.misterius1(12)
dll.misterius2(9)
dll.misterius1(8)
dll.misterius1(62)
dll.misterius1(12)
dll.misterius2(45)

current = dll.head
while current is not None:
    print(current)
    current = current.next
