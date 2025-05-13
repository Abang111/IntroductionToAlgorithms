public class Stack {
    private int[] stack;
    private int top;

    public Stack(int size) {
        stack = new int[size];
        top = -1;
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean push(int value) {
        if (top == stack.length - 1) return false;
        stack[++top] = value;
        return true;
    }

    public Integer pop() {
        if (isEmpty()) return null;
        return stack[top--];
    }

    public static void main(String[] args) {
        Stack s = new Stack(100);
        for (int i = 0; i < 20; i++) s.push(i);
        while (!s.isEmpty()) System.out.println(s.pop());
    }
}