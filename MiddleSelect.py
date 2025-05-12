import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

def middle_select(A, i):
    def select(arr, k):
        if len(arr) <= 5:
            return sorted(arr)[k]
        chunks = [arr[j:j+5] for j in range(0, len(arr), 5)]
        medians = [sorted(chunk)[len(chunk)//2] for chunk in chunks]
        pivot = select(medians, len(medians)//2)
        low = [x for x in arr if x < pivot]
        high = [x for x in arr if x > pivot]
        count = arr.count(pivot)
        if k < len(low):
            return select(low, k)
        elif k < len(low) + count:
            return pivot
        else:
            return select(high, k - len(low) - count)
    return select(A, i)

if __name__ == "__main__":
    print("Now displaying Middle Select")
    A = [random.randint(0, 1000) for _ in range(random.randint(5, 100))]
    print("Array:", A)
    i = random.randint(0, len(A) - 1)
    print(f"The {i}-th smallest element is:", middle_select(A, i))