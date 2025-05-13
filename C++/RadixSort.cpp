#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void countSort(vector<int>& arr, int exp) {
    vector<int> output(arr.size());
    int count[10] = {0};

    for (int num : arr)
        count[(num / exp) % 10]++;

    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (int i = arr.size() - 1; i >= 0; i--) {
        int digit = (arr[i] / exp) % 10;
        output[count[digit] - 1] = arr[i];
        count[digit]--;
    }

    for (int i = 0; i < arr.size(); i++)
        arr[i] = output[i];
}

void radixSort(vector<int>& arr) {
    int maxNum = *max_element(arr.begin(), arr.end());
    for (int exp = 1; maxNum / exp > 0; exp *= 10)
        countSort(arr, exp);
}

int main() {
    vector<int> arr = {170, 45, 75, 90, 802, 24, 2, 66};
    radixSort(arr);
    for (int num : arr)
        cout << num << " ";
    cout << endl;
    return 0;
}