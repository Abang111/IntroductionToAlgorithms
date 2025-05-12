import random
from collections import defaultdict

def radix_sort(arr):
    max_len = len(str(max(arr)))
    for i in range(max_len):
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit = (num // (10 ** i)) % 10
            buckets[digit].append(num)
        arr = [num for bucket in buckets for num in bucket]
    return arr

if __name__ == "__main__":
    print("Now displaying Radix Sort.")
    A = [random.randint(0, 999) for _ in range(random.randint(4, 100))]
    print("Before:", A)
    A = radix_sort(A)
    print("After:", A)