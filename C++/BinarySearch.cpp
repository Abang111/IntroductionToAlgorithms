#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

vector<int> insertionSort(vector<int>& A) {
    for (int j = 1; j < A.size(); j++) {
        int key = A[j];
        int i = j - 1;
        while (i >= 0 && A[i] > key) {
            A[i + 1] = A[i];
            i--;
        }
        A[i + 1] = key;
    }
    return A;
}

int binarySearch(const vector<int>& A, int p, int r, int key) {
    while (p <= r) {
        int q = (p + r) / 2;
        if (A[q] == key) return q;
        else if (A[q] < key) p = q + 1;
        else r = q - 1;
    }
    return -1;
}

int main() {
    srand(time(0));
    int size = rand() % 96 + 5;
    vector<int> A(size);
    for (int i = 0; i < size; i++) {
        A[i] = rand() % 1001;
    }

    insertionSort(A);
    int key = A[rand() % A.size()];

    cout << "Now displaying BinarySearch:\n";
    cout << "Sorted list: ";
    for (int num : A) cout << num << " ";
    cout << "\nKey to search: " << key << endl;
    cout << "Key index: " << binarySearch(A, 0, A.size() - 1, key) << endl;

    return 0;
}
