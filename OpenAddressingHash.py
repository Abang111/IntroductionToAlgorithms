import random

class OpenAddressingHash:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size

    def insert(self, key):
        for i in range(self.size):
            idx = (key + i) % self.size
            if self.table[idx] == -1:
                self.table[idx] = key
                return True
        return False

    def search(self, key):
        for i in range(self.size):
            idx = (key + i) % self.size
            if self.table[idx] == key:
                return idx
        return -1

if __name__ == "__main__":
    print("Now displaying Open Addressing Hash.")
    size = 13
    oah = OpenAddressingHash(size)
    A = [random.randint(0, 1000) for _ in range(random.randint(5, 20))]
    for e in A:
        oah.insert(e)
    print("Hash table:", oah.table)
    e = random.choice(A)
    print(f"The selected element {e} is in slot:", oah.search(e))