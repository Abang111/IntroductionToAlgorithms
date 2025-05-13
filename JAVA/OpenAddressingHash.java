import java.util.Arrays;
import java.util.Random;

public class OpenAddressingHash {
    private int[] table;
    private int size;

    public OpenAddressingHash(int size) {
        this.size = size;
        this.table = new int[size];
        Arrays.fill(this.table, -1);
    }

    public boolean insert(int key) {
        for (int i = 0; i < size; i++) {
            int idx = (key + i) % size;
            if (table[idx] == -1) {
                table[idx] = key;
                return true;
            }
        }
        return false;
    }

    public int search(int key) {
        for (int i = 0; i < size; i++) {
            int idx = (key + i) % size;
            if (table[idx] == key) return idx;
        }
        return -1;
    }

    public static void main(String[] args) {
        OpenAddressingHash hash = new OpenAddressingHash(13);
        int[] keys = {15, 25, 35, 45};
        for (int k : keys) hash.insert(k);
        System.out.println("Index of 25: " + hash.search(25));
    }
}