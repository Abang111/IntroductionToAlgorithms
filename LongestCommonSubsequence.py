# def LCSString(b, X, i, j):
#     if i == -1 or j == -1:
#         return
#     if b[i][j] == "SLOPE":
#         a = LCSString(b, X, i - 1, j - 1)
#         return X[i] if a is None else a + X[i]
#     elif b[i][j] == "UP":
#         return LCSString(b, X, i - 1, j)
#     else:
#         return LCSString(b, X, i, j - 1)
#
# def LCS(X, Y):
#     b = [[0 for i in range(0, len(Y))] for i in range(0, len(X))]
#     c = [[0 for i in range(0, len(Y) + 1)] for i in range(0, len(X) + 1)]
#     for i in range(0, len(X)):
#         for j in range(0, len(Y)):
#             if X[i] == Y[j]:
#                 c[i + 1][j + 1] = c[i][j] + 1
#                 b[i][j] = "SLOPE"
#             elif c[i][j + 1] > c[i + 1][j]:
#                 c[i + 1][j + 1] = c[i][j + 1]
#                 b[i][j] = "UP"
#             else:
#                 c[i + 1][j + 1] = c[i + 1][j]
#                 b[i][j] = "LEFT"
#     return LCSString(b, X, len(X) - 1, len(Y) - 1)
#
# print LCS("ABCBDAB", "BDCABA")
def lcs_string(trace, X, i, j):
    """根据方向表 trace 回溯得到 LCS 字符串"""
    if i < 0 or j < 0:
        return ""
    if trace[i][j] == "SLOPE":
        return lcs_string(trace, X, i - 1, j - 1) + X[i]
    elif trace[i][j] == "UP":
        return lcs_string(trace, X, i - 1, j)
    else:
        return lcs_string(trace, X, i, j - 1)

def lcs(X, Y):
    """计算 X 与 Y 的最长公共子序列"""
    m, n = len(X), len(Y)
    # 动态规划表和方向表
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    trace = [[""] * n for _ in range(m)]

    # 填表
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                trace[i][j] = "SLOPE"
            elif dp[i][j + 1] > dp[i + 1][j]:
                dp[i + 1][j + 1] = dp[i][j + 1]
                trace[i][j] = "UP"
            else:
                dp[i + 1][j + 1] = dp[i + 1][j]
                trace[i][j] = "LEFT"

    return lcs_string(trace, X, m - 1, n - 1)

# ==== 测试 ====
print(lcs("ABCBDAB", "BDCABA"))  # 输出应为 "BCBA" 或 "BDAB"



# 项目	优化内容
# Python 3 兼容	使用 print() 函数
# 命名标准	遵循 PEP 8，函数名小写，变量有意义
# 输出逻辑明确	LCSString() 返回字符串，避免 None 拼接错误
# 边界处理更清晰	初始条件明确（索引从 1 开始）
# 添加注释	每步加解释，便于理解动态规划过程
