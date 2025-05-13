#include <iostream>
#include <string>

class DoublyCircularLinkedList {
public:
    struct Node {
        std::string key;
        Node* prev;
        Node* next;

        Node(const std::string& k) : key(k), prev(nullptr), next(nullptr) {}
    };

    DoublyCircularLinkedList() {
        nil = new Node("NIL");
        nil->next = nil;
        nil->prev = nil;
    }

    ~DoublyCircularLinkedList() {
        Node* current = nil->next;
        while (current != nil) {
            Node* next = current->next;
            delete current;
            current = next;
        }
        delete nil;
    }

    void listInsert(Node* node) {
        node->next = nil->next;
        nil->next->prev = node;
        nil->next = node;
        node->prev = nil;
    }

    Node* listSearch(const std::string& key) {
        Node* x = nil->next;
        while (x != nil && x->key != key) {
            x = x->next;
        }
        return x;
    }

    void listDelete(Node* node) {
        if (node == nil) {
            std::cout << "Attempted to delete NIL node; skipping." << std::endl;
            return;
        }
        node->prev->next = node->next;
        node->next->prev = node->prev;
        delete node;
    }

    std::string display() {
        std::string result;
        Node* x = nil->next;
        while (x != nil) {
            result += x->key + " ";
            x = x->next;
        }
        if (!result.empty()) result.pop_back(); // 去掉最后一个空格
        return result;
    }

    Node* createNode(const std::string& key) {
        return new Node(key);
    }

private:
    Node* nil;
};


