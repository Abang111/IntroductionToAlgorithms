#include <iostream>
#include <vector>

class Fibonacci {
public:
    // 朴素递归（指数时间复杂度）
    static int naiveFibonacci(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        return naiveFibonacci(n - 1) + naiveFibonacci(n - 2);
    }

    // 线性动态规划（O(n)）
    static int linearFibonacci(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        std::vector<int> A(n + 1);
        A[0] = 0;
        A[1] = 1;
        for (int i = 2; i <= n; ++i) {
            A[i] = A[i - 1] + A[i - 2];
        }
        return A[n];
    }

    // 矩阵乘法
    static std::vector<std::vector<int>> matrixMultiply(const std::vector<std::vector<int>>& m1,
                                                        const std::vector<std::vector<int>>& m2) {
        int rows = m1.size();
        int cols = m2[0].size();
        int common = m1[0].size();
        std::vector<std::vector<int>> result(rows, std::vector<int>(cols, 0));

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                for (int k = 0; k < common; ++k) {
                    result[i][j] += m1[i][k] * m2[k][j];
                }
            }
        }
        return result;
    }

    // 快速幂递归计算矩阵的 n 次幂
    static std::vector<std::vector<int>> recursiveSquaring(int n) {
        std::vector<std::vector<int>> base = {{1, 1}, {1, 0}};
        if (n == 0) return {{1, 0}, {0, 1}}; // 单位矩阵
        if (n == 1) return base;

        std::vector<std::vector<int>> half = recursiveSquaring(n / 2);
        std::vector<std::vector<int>> square = matrixMultiply(half, half);

        if (n % 2 == 0) {
            return square;
        } else {
            return matrixMultiply(square, base);
        }
    }

    // 对应的 Fibonacci(n)
    static int logarithmicFibonacci(int n) {
        if (n == 0) return 0;
        std::vector<std::vector<int>> matrix = recursiveSquaring(n);
        return matrix[0][1];
    }
};

// 测试主函数
int main() {
    int n = 20;

    std::cout << "Naive Fibonacci(" << n << "): " << Fibonacci::naiveFibonacci(n) << std::endl;
    std::cout << "Linear Fibonacci(" << n << "): " << Fibonacci::linearFibonacci(n) << std::endl;
    std::cout << "Logarithmic Fibonacci(" << n << "): " << Fibonacci::logarithmicFibonacci(n) << std::endl;

    return 0;
}
