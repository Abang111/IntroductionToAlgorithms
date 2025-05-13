#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

int partition(vector<int>& A, int p, int r) {
    int pivotIndex = p + rand() % (r - p + 1);
    swap(A[p], A[pivotIndex]);
    int pivot = A[p], i = p;
    for (int j = p + 1; j <= r; j++) {
        if (A[j] < pivot) swap(A[++i], A[j]);
    }
    swap(A[p], A[i]);
    return i;
}

void quicksort(vector<int>& A, int p, int r) {
    if (p < r) {
        int q = partition(A, p, r);
        quicksort(A, p, q - 1);
        quicksort(A, q + 1, r);
    }
}

int main() {
    vector<int> A = {3, 6, 8, 10, 1, 2, 1};
    quicksort(A, 0, A.size() - 1);
    for (int v : A) cout << v << " ";
    cout << endl;
    return 0;
}