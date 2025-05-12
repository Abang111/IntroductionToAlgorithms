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
#             i = i-1
#         A[i+1] = key
#     return A
#
# A = []
# s = random.randint(5, 100)
# for i in range(0, s):
#     A.append(random.randint(0, 1000))
# print A
# print InsertionSort(A, len(A))

import random

def insertion_sort(arr):
    """插入排序：升序排列列表"""
    arr = arr[:]  # 拷贝原数组，避免修改原始数据（可选）
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # 将 key 插入到 arr[0...j-1] 的有序子序列中
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

# ==== 测试部分 ====
data = [random.randint(0, 1000) for _ in range(random.randint(5, 100))]
print("Original array:", data)
sorted_data = insertion_sort(data)
print("Sorted array:  ", sorted_data)

# 优化点	原代码	优化后
# Python 3 兼容	print A	print("...", A)
# 命名规范	InsertionSort	insertion_sort
# 调用简化	InsertionSort(A, len(A))	insertion_sort(A)
# 拷贝安全	修改原数组	默认拷贝，防止副作用
# 注释明确	含糊不清	明确说明排序逻辑
