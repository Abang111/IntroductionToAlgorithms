#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& A, int p, int q, int r) {
    vector<int> L(A.begin() + p, A.begin() + q + 1);
    vector<int> R(A.begin() + q + 1, A.begin() + r + 1);
    L.push_back(INT32_MAX);
    R.push_back(INT32_MAX);
    int i = 0, j = 0;
    for (int k = p; k <= r; k++) {
        if (L[i] <= R[j]) A[k] = L[i++];
        else A[k] = R[j++];
    }
}

void mergeSort(vector<int>& A, int p, int r) {
    if (p < r) {
        int q = (p + r) / 2;
        mergeSort(A, p, q);
        mergeSort(A, q + 1, r);
        merge(A, p, q, r);
    }
}

int main() {
    vector<int> A = {5, 2, 4, 7, 1, 3, 2, 6};
    mergeSort(A, 0, A.size() - 1);
    for (int x : A) cout << x << " ";
    cout << endl;
    return 0;
}