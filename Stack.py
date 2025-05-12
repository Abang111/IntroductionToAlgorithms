class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

if __name__ == "__main__":
    import random
    s = Stack()
    for _ in range(20):
        s.push(random.randint(0, 999))
    while not s.is_empty():
        print(s.pop())