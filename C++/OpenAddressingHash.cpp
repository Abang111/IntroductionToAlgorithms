#include <iostream>
#include <vector>
using namespace std;

class OpenAddressingHash {
    vector<int> table;
    int size;

public:
    OpenAddressingHash(int s) : size(s), table(s, -1) {}

    bool insert(int key) {
        for (int i = 0; i < size; i++) {
            int idx = (key + i) % size;
            if (table[idx] == -1) {
                table[idx] = key;
                return true;
            }
        }
        return false;
    }

    int search(int key) {
        for (int i = 0; i < size; i++) {
            int idx = (key + i) % size;
            if (table[idx] == key) return idx;
        }
        return -1;
    }

    void print() {
        for (int v : table)
            cout << v << " ";
        cout << endl;
    }
};

int main() {
    OpenAddressingHash hash(13);
    int keys[] = {15, 25, 35, 45};
    for (int k : keys) hash.insert(k);
    hash.print();
    cout << "Index of 25: " << hash.search(25) << endl;
    return 0;
}