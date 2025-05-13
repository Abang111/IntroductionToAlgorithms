#include <iostream>
using namespace std;

long long fastPow(long long x, int n) {
    long long result = 1;
    while (n > 0) {
        if (n % 2 == 1) result *= x;
        x *= x;
        n /= 2;
    }
    return result;
}

int main() {
    long long x = 2;
    int n = 10;
    cout << x << " to the power " << n << " is: " << fastPow(x, n) << endl;
    return 0;
}