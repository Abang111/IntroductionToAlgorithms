import random

def merge_sort(A):
    def merge_sort_recursive(A, p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort_recursive(A, p, q)
            merge_sort_recursive(A, q + 1, r)
            merge(A, p, q, r)

    def merge(A, p, q, r):
        L = A[p:q+1]
        R = A[q+1:r+1]
        i = j = 0
        k = p

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

    merge_sort_recursive(A, 0, len(A) - 1)

if __name__ == "__main__":
    print("Now displaying MergeSort")
    A = [random.randint(0, 1000) for _ in range(random.randint(5, 100))]
    print("Before:", A)
    merge_sort(A)
    print("After:", A)