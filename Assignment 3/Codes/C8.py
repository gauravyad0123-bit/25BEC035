class CircularQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError('capacity must be positive')
        self.data = [None] * capacity
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.size == len(self.data):
            raise OverflowError('queue is full')
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return item

    def first(self):
        if self.is_empty():
            raise IndexError('first from empty queue')
        return self.data[self.front]