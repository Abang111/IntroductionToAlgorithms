import random

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def partition(A, p, r):
    pivot_index = random.randint(p, r)
    A[p], A[pivot_index] = A[pivot_index], A[p]
    pivot = A[p]
    i = p
    for j in range(p + 1, r + 1):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[p], A[i] = A[i], A[p]
    return i

if __name__ == "__main__":
    print("Now displaying QuickSort")
    A = [random.randint(0, 1000) for _ in range(random.randint(5, 100))]
    print("Before:", A)
    quicksort(A, 0, len(A) - 1)
    print("After:", A)