#include <iostream>
#include <vector>
#include <algorithm> // for std::copy
using namespace std;

class HeapSort {
public:
    // 保持最大堆性质
    static void maxHeapify(vector<int>& arr, int i, int heapSize) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int largest = i;

        if (left < heapSize && arr[left] > arr[largest]) {
            largest = left;
        }
        if (right < heapSize && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest != i) {
            swap(arr[i], arr[largest]);
            maxHeapify(arr, largest, heapSize);
        }
    }

    // 构建最大堆
    static void buildMaxHeap(vector<int>& arr) {
        int heapSize = arr.size();
        for (int i = heapSize / 2 - 1; i >= 0; i--) {
            maxHeapify(arr, i, heapSize);
        }
    }

    // 堆排序，返回升序副本
    static vector<int> heapSort(const vector<int>& arr) {
        vector<int> sorted = arr;
        buildMaxHeap(sorted);
        int heapSize = sorted.size();

        for (int i = sorted.size() - 1; i > 0; i--) {
            swap(sorted[0], sorted[i]);
            heapSize--;
            maxHeapify(sorted, 0, heapSize);
        }
        return sorted;
    }

    // 打印工具
    static void printVector(const vector<int>& vec, const string& label) {
        cout << label;
        for (int val : vec) {
            cout << val << " ";
        }
        cout << endl;
    }
};

// 测试主函数
int main() {
    vector<int> data = {23, 1, 45, 78, 3, 5, 9};
    HeapSort::printVector(data, "Original: ");
    vector<int> sorted = HeapSort::heapSort(data);
    HeapSort::printVector(sorted, "Sorted:   ");
    return 0;
}
