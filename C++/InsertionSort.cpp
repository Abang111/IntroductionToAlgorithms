#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <iomanip>

using namespace std;

class InsertionSort {
public:
    // 插入排序：返回升序副本
    static vector<int> insertionSort(const vector<int>& arr) {
        vector<int> sorted = arr; // 拷贝原数组
        for (size_t j = 1; j < sorted.size(); ++j) {
            int key = sorted[j];
            int i = j - 1;
            while (i >= 0 && sorted[i] > key) {
                sorted[i + 1] = sorted[i];
                --i;
            }
            sorted[i + 1] = key;
        }
        return sorted;
    }

    // 打印 vector
    static void printVector(const vector<int>& vec, const string& label) {
        cout << label;
        for (int val : vec) {
            cout << val << " ";
        }
        cout << endl;
    }
};

// 主函数：测试
int main() {
    srand(time(0)); // 初始化随机种子

    int size = rand() % 96 + 5; // [5, 100]
    vector<int> data(size);
    for (int i = 0; i < size; ++i) {
        data[i] = rand() % 1001; // [0, 1000]
    }

    InsertionSort::printVector(data, "Original array: ");
    vector<int> sortedData = InsertionSort::insertionSort(data);
    InsertionSort::printVector(sortedData, "Sorted array:   ");

    return 0;
}
