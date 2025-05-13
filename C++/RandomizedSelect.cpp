#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

int partition(vector<int>& A, int p, int r) {
    int pivotIndex = p + rand() % (r - p + 1);
    swap(A[p], A[pivotIndex]);
    int pivot = A[p], i = p;
    for (int j = p + 1; j <= r; j++) {
        if (A[j] < pivot)
            swap(A[++i], A[j]);
    }
    swap(A[p], A[i]);
    return i;
}

int randomizedSelect(vector<int>& A, int p, int r, int i) {
    if (p == r) return A[p];
    int q = partition(A, p, r);
    int k = q - p;
    if (i == k) return A[q];
    else if (i < k) return randomizedSelect(A, p, q - 1, i);
    else return randomizedSelect(A, q + 1, r, i - k - 1);
}

int main() {
    vector<int> A = {9, 3, 2, 7, 1, 5, 4};
    int i = 3;
    cout << "Element at index " << i << " is: " << randomizedSelect(A, 0, A.size() - 1, i) << endl;
    return 0;
}