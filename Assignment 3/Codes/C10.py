def add_first(data, front, size, item):
    if size == len(data):
        raise OverflowError('deque is full')
    front = (front - 1) % len(data)
    data[front] = item
    return front, size + 1

def add_last(data, front, size, item):
    if size == len(data):
        raise OverflowError('deque is full')
    rear = (front + size) % len(data)
    data[rear] = item
    return front, size + 1

def delete_first(data, front, size):
    if size == 0:
        raise IndexError('empty deque')
    item = data[front]
    data[front] = None
    front = (front + 1) % len(data)
    return item, front, size - 1

def delete_last(data, front, size):
    if size == 0:
        raise IndexError('empty deque')
    rear = (front + size - 1) % len(data)
    item = data[rear]
    data[rear] = None
    return item, front, size - 1