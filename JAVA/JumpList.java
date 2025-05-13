import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class Node {
    int key;
    Node next;
    Node prev;
    Node down;

    Node(int key) {
        this.key = key;
        this.next = null;
        this.prev = null;
        this.down = null;
    }
}

class LevelList {
    Node head;
    Node tail;

    LevelList() {
        head = new Node(-1);       // -∞ sentinel
        tail = new Node(10000);    // +∞ sentinel
        head.next = tail;
        tail.prev = head;
    }
}

public class JumpList {
    List<LevelList> levels;
    Random rand;

    public JumpList() {
        levels = new ArrayList<>();
        levels.add(new LevelList());  // Level 0
        rand = new Random();
    }

    public void addLevel() {
        LevelList newLevel = new LevelList();
        newLevel.head.down = levels.get(levels.size() - 1).head;
        newLevel.tail.down = levels.get(levels.size() - 1).tail;
        levels.add(newLevel);
    }

    public void insert(int key) {
        int level = 0;
        while (rand.nextInt(2) == 0) level++;
        while (levels.size() <= level) addLevel();

        Node newNode = new Node(key);
        Node current = levels.get(level).head;

        // Find insert position on top level
        while (current.next.key < key) {
            current = current.next;
        }

        // Insert node
        newNode.next = current.next;
        newNode.prev = current;
        current.next.prev = newNode;
        current.next = newNode;

        // Insert downward recursively
        insertDown(newNode, newNode.prev.down, key);
    }

    private void insertDown(Node upperNode, Node downNode, int key) {
        if (downNode == null) return;

        Node newNode = new Node(key);
        upperNode.down = newNode;

        Node current = downNode;
        while (current.next.key < key) {
            current = current.next;
        }

        newNode.next = current.next;
        newNode.prev = current;
        current.next.prev = newNode;
        current.next = newNode;

        insertDown(newNode, newNode.prev.down, key);
    }

    public Node search(int key) {
        Node current = levels.get(levels.size() - 1).head;
        while (current != null) {
            while (current.next != null && current.next.key <= key) {
                current = current.next;
            }
            if (current.key == key) return current;
            current = current.down;
        }
        return null;
    }

    public boolean delete(int key) {
        Node current = levels.get(levels.size() - 1).head;
        boolean found = false;

        while (current != null) {
            while (current.next != null && current.next.key < key) {
                current = current.next;
            }

            if (current.next != null && current.next.key == key) {
                Node target = current.next;
                current.next = target.next;
                target.next.prev = current;
                found = true;
                current = current.down;
            } else {
                current = current.down;
            }
        }

        return found;
    }

    // Optional: print skip list from top to bottom
    public void print() {
        for (int i = levels.size() - 1; i >= 0; i--) {
            Node current = levels.get(i).head;
            System.out.print("Level " + i + ": ");
            while (current != null) {
                System.out.print(current.key + " ");
                current = current.next;
                if (current != null && current.key == 10000) break;
            }
            System.out.println();
        }
    }
}