public class PowerProblem {
    public static long fastPow(long x, int n) {
        long result = 1;
        while (n > 0) {
            if ((n & 1) == 1) result *= x;
            x *= x;
            n >>= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        long x = 2;
        int n = 10;
        System.out.println(x + " to the power " + n + " is: " + fastPow(x, n));
    }
}