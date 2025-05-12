# import random
# #
# #
# # def MaxHeapify(A, i, s):
# #     l = i * 2
# #     r = i * 2 + 1
# #     largest = i
# #     if l < s and A[l] > A[i]:
# #         largest = l
# #     if r < s and A[r] > A[largest]:
# #         largest = r
# #     if largest != i:
# #         A[i], A[largest] = A[largest], A[i]
# #         MaxHeapify(A, largest, s)
# #
# #
# # def BuildMaxHeap(A, s):
# #     for i in range(0, len(A) / 2)[::-1]:
# #         MaxHeapify(A, i, s)
# #     return A
# #
# #
# # def HeapSort(A):
# #     s = len(A)
# #     BuildMaxHeap(A, s)
# #
# #     for i in range(1, len(A))[::-1]:
# #         A[0], A[i] = A[i], A[0]
# #         s -= 1
# #         MaxHeapify(A, 0, s)
# #     return A
# #
# #
# # print "Now displaying HeapSort"
# # A = []
# # s = random.randint(5, 100)
# # for i in range(0, s):
# #     A.append(random.randint(0, 1000))
# # print A
# # print HeapSort(A)

import random

def max_heapify(arr, i, heap_size):
    """保持最大堆性质：调整以 i 为根的子树"""
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)

def build_max_heap(arr):
    """从无序数组构建最大堆"""
    heap_size = len(arr)
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(arr, i, heap_size)

def heap_sort(arr):
    """堆排序主函数：升序排列数组"""
    arr = arr[:]  # 创建副本，避免原数组被修改（可选）
    build_max_heap(arr)
    heap_size = len(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size)
    return arr

# ==== 测试部分 ====
print("Now displaying HeapSort")
A = [random.randint(0, 1000) for _ in range(random.randint(5, 100))]
print("Original array:", A)
sorted_array = heap_sort(A)
print("Sorted array:", sorted_array)

# 优化项	原始写法	优化后写法
# print语法	print A	print("A:", A)
# 除法运算	len(A) / 2	len(A) // 2
# range 反向迭代	range(...)[::-1]	range(..., ..., -1)
# 索引起始	l = i*2	left = 2*i + 1
# 排序不改原数组（可选）	原地排序	拷贝后排序
