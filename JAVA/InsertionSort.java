import java.util.Arrays;
import java.util.Random;

public class InsertionSort {

    // 插入排序：返回升序副本
    public static int[] insertionSort(int[] arr) {
        int[] sorted = Arrays.copyOf(arr, arr.length); // 拷贝原数组
        for (int j = 1; j < sorted.length; j++) {
            int key = sorted[j];
            int i = j - 1;
            // 将 key 插入到 sorted[0...j-1] 的有序子序列中
            while (i >= 0 && sorted[i] > key) {
                sorted[i + 1] = sorted[i];
                i--;
            }
            sorted[i + 1] = key;
        }
        return sorted;
    }
}
