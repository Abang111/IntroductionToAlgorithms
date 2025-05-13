import java.util.Arrays;

public class HeapSort {

    // 保持最大堆性质
    public static void maxHeapify(int[] arr, int i, int heapSize) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int largest = i;

        if (left < heapSize && arr[left] > arr[largest]) {
            largest = left;
        }
        if (right < heapSize && arr[right] > arr[largest]) {
            largest = right;
        }

        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            maxHeapify(arr, largest, heapSize);
        }
    }

    // 构建最大堆
    public static void buildMaxHeap(int[] arr) {
        int heapSize = arr.length;
        for (int i = (heapSize / 2) - 1; i >= 0; i--) {
            maxHeapify(arr, i, heapSize);
        }
    }

    // 堆排序：返回升序副本
    public static int[] heapSort(int[] arr) {
        int[] sorted = Arrays.copyOf(arr, arr.length);
        buildMaxHeap(sorted);
        int heapSize = sorted.length;
        for (int i = sorted.length - 1; i > 0; i--) {
            int temp = sorted[0];
            sorted[0] = sorted[i];
            sorted[i] = temp;
            heapSize--;
            maxHeapify(sorted, 0, heapSize);
        }
        return sorted;
    }
}