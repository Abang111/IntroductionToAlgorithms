import java.util.Random;

public class QuickSort {
    static Random rand = new Random();

    public static void quicksort(int[] A, int p, int r) {
        if (p < r) {
            int q = partition(A, p, r);
            quicksort(A, p, q - 1);
            quicksort(A, q + 1, r);
        }
    }

    public static int partition(int[] A, int p, int r) {
        int pivotIndex = p + rand.nextInt(r - p + 1);
        int pivot = A[pivotIndex];
        swap(A, p, pivotIndex);
        int i = p;
        for (int j = p + 1; j <= r; j++) {
            if (A[j] < pivot) {
                i++;
                swap(A, i, j);
            }
        }
        swap(A, p, i);
        return i;
    }

    private static void swap(int[] A, int i, int j) {
        int tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }

    public static void main(String[] args) {
        int[] A = {3, 6, 8, 10, 1, 2, 1};
        quicksort(A, 0, A.length - 1);
        for (int v : A) System.out.print(v + " ");
    }
}