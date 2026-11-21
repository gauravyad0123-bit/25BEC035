class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty stack')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError('top from empty stack')
        return self._data[-1]

s = Stack()
s.push(10); s.push(20)
print(s.top())   # 20
print(s.pop())   # 20
print(len(s))    # 1