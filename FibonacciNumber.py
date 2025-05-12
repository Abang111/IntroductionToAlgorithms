# import random
#
#
# def NaiveFibonacci(a):
#     if a == 0:
#         return 0
#     if a == 1:
#         return 1
#     else:
#         return NaiveFibonacci(a - 1) + NaiveFibonacci(a - 2)
#
#
# def LinearFibonacci(a):
#     A = [0, 1]
#     for i in range(2, a + 1):
#         A.append(A[i - 1] + A[i - 2])
#     return A[a]
#
#
# def MatrixMultiply(m1, m2):
#     result = [[0 for i in range(len(m2[0]))] for i in range(len(m1))]
#     for i in range(0, len(m1)):  # The number of the row is defined by m1
#         for j in range(0, len(m2[0])):  # The number of column is defined by m2
#             for k in range(len(m1[0])):
#                 result[i][j] += m1[i][k] * m2[k][j]
#     return result
#
#
# def RecursiveSquaring(n):
#     basicMatrix = [[1, 1], [1, 0]]
#     if n == 0:
#         return basicMatrix  # Identity matrix
#     if n == 1:
#         return basicMatrix
#     else:
#         matrix = RecursiveSquaring(n / 2)
#         if n % 2 == 0:
#             return MatrixMultiply(matrix, matrix)
#         if n % 2 == 1:
#             return MatrixMultiply(MatrixMultiply(matrix, matrix), basicMatrix)
#
#
# def AdvanceFibonacci(n):
#     matrix = RecursiveSquaring(n)
#     return matrix[0][1]
#
#
# a = random.randint(0, 100)
# print "Now Displaying Fibonacci Number(Naive Method)"
# print "the Fibonacci number of ", a, " is ", NaiveFibonacci(a)
# print "Now Displaying Fibonacci Number(Linear)"
# print "the Fibonacci number of ", a, " is ", LinearFibonacci(a)
# print "Now Displaying Fibonacci Number(logn)"
# print "the Fibonacci number of ", a, " is ", AdvanceFibonacci(a)

import random

def naive_fibonacci(n: int) -> int:
    """递归方式计算斐波那契数列（指数时间复杂度）"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)

def linear_fibonacci(n: int) -> int:
    """线性时间斐波那契计算（迭代 DP）"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    A = [0, 1]
    for i in range(2, n + 1):
        A.append(A[i - 1] + A[i - 2])
    return A[n]

def matrix_multiply(m1: list, m2: list) -> list:
    """矩阵乘法"""
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def recursive_squaring(n: int) -> list:
    """使用快速矩阵幂计算 Fibonacci，复杂度 O(log n)"""
    base_matrix = [[1, 1], [1, 0]]
    if n == 0:
        return [[1, 0], [0, 1]]  # 单位矩阵
    if n == 1:
        return base_matrix
    half = recursive_squaring(n // 2)
    square = matrix_multiply(half, half)
    if n % 2 == 0:
        return square
    else:
        return matrix_multiply(square, base_matrix)

def logarithmic_fibonacci(n: int) -> int:
    """主调用：矩阵快速幂方式计算第 n 个 Fibonacci 数"""
    if n == 0:
        return 0
    matrix = recursive_squaring(n)
    return matrix[0][1]

# ==== 测试部分 ====
a = random.randint(0, 30)  # 控制小范围以避免 naive 方法耗时过长

print("Now Displaying Fibonacci Number (Naive Method)")
print(f"The Fibonacci number of {a} is {naive_fibonacci(a)}")

print("Now Displaying Fibonacci Number (Linear DP)")
print(f"The Fibonacci number of {a} is {linear_fibonacci(a)}")

print("Now Displaying Fibonacci Number (Logarithmic Matrix)")
print(f"The Fibonacci number of {a} is {logarithmic_fibonacci(a)}")

# 命名风格	函数统一为小写 + 下划线命名	遵守 PEP8，增强可读性与一致性
# 输出语法	使用 print() 格式化字符串	符合 Python 3，便于调试
# 除法逻辑	使用 // 替代 /	保证整数索引有效，避免 list index error
# 异常输入处理	对 n=0 单独处理	避免矩阵计算中出现不必要错误
# 结构化设计	保留 3 种算法用于对比测试	有利于算法学习和复杂度比较
