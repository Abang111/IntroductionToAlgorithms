import java.util.List;

public class BinarySearch {
    public static List<Integer> insertionSort(List<Integer> A) {
        for (int j = 1; j < A.size(); j++) {
            int key = A.get(j);
            int i = j - 1;
            while (i >= 0 && A.get(i) > key) {
                A.set(i + 1, A.get(i));
                i--;
            }
            A.set(i + 1, key);
        }
        return A;
    }

    public static int binarySearch(List<Integer> A, int p, int r, int key) {
        while (p <= r) {
            int q = (p + r) / 2;
            if (A.get(q) == key) return q;
            else if (A.get(q) < key) p = q + 1;
            else r = q - 1;
        }
        return -1;
    }
}
