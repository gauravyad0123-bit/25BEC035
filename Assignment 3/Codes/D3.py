class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, element):
        newest = Node(element, self.head)
        self.head = newest
        if self.size == 0:
            self.tail = newest
        self.size += 1

    def insert_last(self, element):
        newest = Node(element)
        if self.size == 0:
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def delete_first(self):
        if self.size == 0:
            raise IndexError('delete from empty list')
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return answer

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.element)
            current = current.next