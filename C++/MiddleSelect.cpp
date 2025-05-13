#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int select(vector<int> arr, int k);

int getMedian(vector<int> arr) {
    sort(arr.begin(), arr.end());
    return arr[arr.size() / 2];
}

int select(vector<int> arr, int k) {
    if (arr.size() <= 5) {
        sort(arr.begin(), arr.end());
        return arr[k];
    }

    vector<int> medians;
    for (size_t i = 0; i < arr.size(); i += 5) {
        size_t end = min(i + 5, arr.size());
        vector<int> group(arr.begin() + i, arr.begin() + end);
        medians.push_back(getMedian(group));
    }

    int pivot = select(medians, medians.size() / 2);

    vector<int> low, high, equal;
    for (int val : arr) {
        if (val < pivot) low.push_back(val);
        else if (val > pivot) high.push_back(val);
        else equal.push_back(val);
    }

    if (k < low.size()) return select(low, k);
    else if (k < low.size() + equal.size()) return pivot;
    else return select(high, k - low.size() - equal.size());
}

int main() {
    vector<int> arr = {7, 10, 4, 3, 20, 15};
    int k = 2;
    cout << "K-th smallest element is: " << select(arr, k) << endl;
    return 0;
}