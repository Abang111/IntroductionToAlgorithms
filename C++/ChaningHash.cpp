#include <iostream>
#include <vector>
#include <list>
#include <cstdlib>
#include <ctime>

using namespace std;

const int SLOT_SIZE = 13;

void hashInsert(int key, vector<list<int>>& table) {
    int index = key % SLOT_SIZE;
    table[index].push_back(key);
}

pair<int, int> hashSearch(int key, const vector<list<int>>& table) {
    int index = key % SLOT_SIZE;
    int pos = 0;
    for (int val : table[index]) {
        if (val == key) return {index, pos};
        pos++;
    }
    return {-1, -1};
}

void hashDelete(int key, vector<list<int>>& table) {
    int index = key % SLOT_SIZE;
    auto& chain = table[index];
    for (auto it = chain.begin(); it != chain.end(); ++it) {
        if (*it == key) {
            chain.erase(it);
            break;
        }
    }
}

int main() {
    srand(time(0));
    int dataSize = rand() % 96 + 5;
    vector<int> data(dataSize);
    vector<list<int>> hashTable(SLOT_SIZE);

    for (int i = 0; i < dataSize; ++i) {
        data[i] = rand() % 1001;
        hashInsert(data[i], hashTable);
    }

    cout << "Now displaying Chaining Hash" << endl;
    cout << "Hash Table:\n";
    for (int i = 0; i < SLOT_SIZE; ++i) {
        cout << "Slot " << i << ": ";
        for (int val : hashTable[i]) cout << val << " ";
        cout << endl;
    }

    int target = data[rand() % data.size()];
    auto [slot, pos] = hashSearch(target, hashTable);
    if (slot != -1)
        cout << "The selected element " << target << " is in Slot " << slot << ", Position " << pos << endl;
    else
        cout << "The selected element " << target << " was not found in the table." << endl;

    hashDelete(target, hashTable);

    cout << "After Deletion:\n";
    for (int i = 0; i < SLOT_SIZE; ++i) {
        cout << "Slot " << i << ": ";
        for (int val : hashTable[i]) cout << val << " ";
        cout << endl;
    }

    return 0;
}
