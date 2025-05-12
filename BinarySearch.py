# import random
#
#
# def InsertionSort(A, n):
#     for j in range(1, n):
#         key = A[j]
#         # Insert A[j] into the sorted sequence[1...j-1]
#         i = j - 1
#         while i >= 0 and A[i] > key:
#             A[i + 1] = A[i]
#             i = i - 1
#         A[i + 1] = key
#     return A
#
#
# def BinarySearch(A, p, r, key):
#     if p >= r:
#         return -1
#     q = (p + r) / 2
#     if A[q] == key:
#         return q
#     elif A[q] < key:
#         return BinarySearch(A, q + 1, r, key)
#     else:
#         return BinarySearch(A, p, q, key)
#
#
# # Pre procedure.
# A = []
# s = random.randint(5, 100)
# for i in range(0, s):
#     A.append(random.randint(0, 1000))
# A = InsertionSort(A, len(A))
# key = random.choice(A)
#
# print "Now displaying BinarySearch."
# print A
# print key
# print BinarySearch(A, 0, len(A) - 1, key)

import random
from typing import List

def insertion_sort(A: List[int]) -> List[int]:
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

def binary_search(A: List[int], p: int, r: int, key: int) -> int:
    while p <= r:
        q = (p + r) // 2
        if A[q] == key:
            return q
        elif A[q] < key:
            p = q + 1
        else:
            r = q - 1
    return -1

# Generate random sorted list
A = [random.randint(0, 1000) for _ in range(random.randint(5, 100))]
A = insertion_sort(A)

# Pick a random key from the list
key = random.choice(A)

# Display results
print("Now displaying BinarySearch:")
print("Sorted list:", A)
print("Key to search:", key)
print("Key index:", binary_search(A, 0, len(A) - 1, key))
# ✅ 优化点说明：
# 兼容 Python 3：print 改为函数形式。
#
# 修复 BinarySearch 中浮点索引问题：q = (p + r) // 2 替代 /。
#
# 添加类型注解和更清晰的结构。
#
# 逻辑优化：在 BinarySearch 中使用更标准的边界处理（含等于边界时也判断）。
#
# 生成数据清晰可控。
