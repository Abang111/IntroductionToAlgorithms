#include <iostream>
using namespace std;

class CircularQueue {
private:
    int* data;
    int head, tail, size;

public:
    CircularQueue(int capacity) {
        size = capacity;
        data = new int[size];
        head = tail = 0;
    }

    ~CircularQueue() {
        delete[] data;
    }

    bool isEmpty() {
        return head == tail;
    }

    bool isFull() {
        return (tail + 1) % size == head;
    }

    bool enqueue(int val) {
        if (isFull()) return false;
        data[tail] = val;
        tail = (tail + 1) % size;
        return true;
    }

    int dequeue() {
        if (isEmpty()) return -1;
        int val = data[head];
        head = (head + 1) % size;
        return val;
    }
};

int main() {
    CircularQueue q(10);
    for (int i = 0; i < 9; ++i) q.enqueue(i);
    while (!q.isEmpty()) cout << q.dequeue() << endl;
    return 0;
}