import random

def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k - 1)

def randomized_partition(A, p, r):
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
    print("Now displaying Randomized Select")
    A = [random.randint(0, 100000000) for _ in range(random.randint(5, 100))]
    idx = random.randint(0, len(A) - 1)
    result = randomized_select(A, 0, len(A) - 1, idx)
    print(f"The {idx}-th smallest element is:", result)
    print("Correct (sorted):", sorted(A)[idx])