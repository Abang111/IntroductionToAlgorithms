public class FibonacciNumber {


        // 递归方式（指数时间复杂度）
        public static int naiveFibonacci(int n) {
            if (n == 0) return 0;
            if (n == 1) return 1;
            return naiveFibonacci(n - 1) + naiveFibonacci(n - 2);
        }

        // 线性 DP（时间复杂度 O(n)）
        public static int linearFibonacci(int n) {
            if (n == 0) return 0;
            if (n == 1) return 1;

            int[] A = new int[n + 1];
            A[0] = 0;
            A[1] = 1;
            for (int i = 2; i <= n; i++) {
                A[i] = A[i - 1] + A[i - 2];
            }
            return A[n];
        }

        // 矩阵乘法
        public static int[][] matrixMultiply(int[][] m1, int[][] m2) {
            int rows = m1.length;
            int cols = m2[0].length;
            int common = m1[0].length;
            int[][] result = new int[rows][cols];

            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    for (int k = 0; k < common; k++) {
                        result[i][j] += m1[i][k] * m2[k][j];
                    }
                }
            }
            return result;
        }

        // 快速幂法递归计算矩阵的 n 次幂
        public static int[][] recursiveSquaring(int n) {
            int[][] base = {{1, 1}, {1, 0}};
            if (n == 0) return new int[][]{{1, 0}, {0, 1}}; // 单位矩阵
            if (n == 1) return base;

            int[][] half = recursiveSquaring(n / 2);
            int[][] square = matrixMultiply(half, half);

            if (n % 2 == 0) {
                return square;
            } else {
                return matrixMultiply(square, base);
            }
        }

        // 主函数：快速幂法 Fibonacci
        public static int logarithmicFibonacci(int n) {
            if (n == 0) return 0;
            int[][] matrix = recursiveSquaring(n);
            return matrix[0][1];
        }
}
