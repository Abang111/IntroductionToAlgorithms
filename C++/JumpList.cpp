#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Node {
    int key;
    Node* next;
    Node* prev;
    Node* down;

    Node(int k) : key(k), next(nullptr), prev(nullptr), down(nullptr) {}
};

struct LevelList {
    Node* head;
    Node* tail;

    LevelList() {
        head = new Node(-1);     // -∞
        tail = new Node(10000);  // +∞
        head->next = tail;
        tail->prev = head;
    }
};

class SkipList {
public:
    vector<LevelList*> levels;

    SkipList() {
        levels.push_back(new LevelList());  // Level 0
        srand((unsigned int)time(nullptr)); // 初始化随机种子
    }

    ~SkipList() {
        for (LevelList* level : levels) {
            Node* current = level->head;
            while (current) {
                Node* next = current->next;
                delete current;
                current = next;
            }
            delete level;
        }
    }

    void addLevel() {
        LevelList* newLevel = new LevelList();
        newLevel->head->down = levels.back()->head;
        newLevel->tail->down = levels.back()->tail;
        levels.push_back(newLevel);
    }

    void insert(int key) {
        int level = 0;
        while (rand() % 2 == 0) level++;
        while ((int)levels.size() <= level) addLevel();

        Node* newNode = new Node(key);
        Node* current = levels[level]->head;

        // 寻找插入位置（最上层）
        while (current->next->key < key) {
            current = current->next;
        }

        // 插入当前层
        newNode->next = current->next;
        newNode->prev = current;
        current->next->prev = newNode;
        current->next = newNode;

        // 向下插入
        insertDown(newNode, newNode->prev->down, key);
    }

    void insertDown(Node* upperNode, Node* downNode, int key) {
        if (!downNode) return;

        Node* newNode = new Node(key);
        upperNode->down = newNode;

        Node* current = downNode;
        while (current->next->key < key) {
            current = current->next;
        }

        newNode->next = current->next;
        newNode->prev = current;
        current->next->prev = newNode;
        current->next = newNode;

        insertDown(newNode, newNode->prev->down, key);
    }

    Node* search(int key) {
        Node* current = levels.back()->head;
        while (current) {
            while (current->next && current->next->key <= key) {
                current = current->next;
            }
            if (current->key == key) return current;
            current = current->down;
        }
        return nullptr;
    }

    bool deleteKey(int key) {
        Node* current = levels.back()->head;
        bool found = false;

        while (current) {
            while (current->next && current->next->key < key) {
                current = current->next;
            }

            if (current->next && current->next->key == key) {
                Node* target = current->next;
                current->next = target->next;
                target->next->prev = current;
                delete target;
                found = true;
                current = current->down;
            } else {
                current = current->down;
            }
        }

        return found;
    }

    void print() {
        for (int i = (int)levels.size() - 1; i >= 0; --i) {
            Node* current = levels[i]->head;
            cout << "Level " << i << ": ";
            while (current) {
                cout << current->key << " ";
                current = current->next;
                if (current && current->key == 10000) break;
            }
            cout << endl;
        }
    }
};

// === 测试主函数 ===
int main() {
    SkipList sl;
    for (int i = 1; i <= 10; ++i) {
        sl.insert(i * 10);
    }

    sl.print();

    int key = 50;
    cout << "Searching for " << key << ": " << (sl.search(key) != nullptr ? "Found" : "Not found") << endl;
    cout << "Deleting " << key << ": " << (sl.deleteKey(key) ? "Deleted" : "Not found") << endl;
    sl.print();

    return 0;
}
