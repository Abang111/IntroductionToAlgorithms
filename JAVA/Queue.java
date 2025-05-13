public class Queue {
    private int[] queue;
    private int head;
    private int tail;
    private int size;

    public Queue(int size) {
        this.size = size;
        this.queue = new int[size];
        this.head = 0;
        this.tail = 0;
    }

    public boolean isEmpty() {
        return head == tail;
    }

    public boolean isFull() {
        return (tail + 1) % size == head;
    }

    public boolean enqueue(int value) {
        if (isFull()) return false;
        queue[tail] = value;
        tail = (tail + 1) % size;
        return true;
    }

    public Integer dequeue() {
        if (isEmpty()) return null;
        int value = queue[head];
        head = (head + 1) % size;
        return value;
    }

    public static void main(String[] args) {
        Queue q = new Queue(10);
        for (int i = 0; i < 9; i++) q.enqueue(i);
        while (!q.isEmpty()) System.out.println(q.dequeue());
    }
}