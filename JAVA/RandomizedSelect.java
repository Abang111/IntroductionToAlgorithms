import java.util.*;

public class RandomizedSelect {
    static Random rand = new Random();

    public static int randomizedSelect(int[] A, int p, int r, int i) {
        if (p == r) return A[p];
        int q = randomizedPartition(A, p, r);
        int k = q - p;
        if (i == k) return A[q];
        else if (i < k) return randomizedSelect(A, p, q - 1, i);
        else return randomizedSelect(A, q + 1, r, i - k - 1);
    }

    public static int randomizedPartition(int[] A, int p, int r) {
        int pivotIndex = p + rand.nextInt(r - p + 1);
        swap(A, p, pivotIndex);
        int pivot = A[p], i = p;
        for (int j = p + 1; j <= r; j++) {
            if (A[j] < pivot) swap(A, ++i, j);
        }
        swap(A, p, i);
        return i;
    }

    private static void swap(int[] A, int i, int j) {
        int tmp = A[i]; A[i] = A[j]; A[j] = tmp;
    }

    public static void main(String[] args) {
        int[] A = {9, 3, 2, 7, 1, 5, 4};
        int i = 3;
        System.out.println("Element at index " + i + " is: " + randomizedSelect(A, 0, A.length - 1, i));
    }
}