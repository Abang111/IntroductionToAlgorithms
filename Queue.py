class CircularQueue:
    def __init__(self, size=10):
        self.size = size
        self.queue = [None] * size
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def enqueue(self, value):
        if self.is_full():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        val = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        return val

if __name__ == "__main__":
    q = CircularQueue()
    for i in range(9):  # Only size - 1 elements allowed
        q.enqueue(i)
    while not q.is_empty():
        print(q.dequeue())