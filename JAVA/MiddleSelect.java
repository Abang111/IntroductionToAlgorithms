import java.util.*;

public class MiddleSelect {
    public static int select(int[] arr, int k) {
        if (arr.length <= 5) {
            Arrays.sort(arr);
            return arr[k];
        }

        int n = arr.length;
        int numMedians = (n + 4) / 5;
        int[] medians = new int[numMedians];
        for (int i = 0; i < numMedians; i++) {
            int start = i * 5;
            int end = Math.min(start + 5, n);
            int[] group = Arrays.copyOfRange(arr, start, end);
            Arrays.sort(group);
            medians[i] = group[group.length / 2];
        }

        int pivot = select(medians, medians.length / 2);
        List<Integer> lows = new ArrayList<>(), highs = new ArrayList<>(), pivots = new ArrayList<>();
        for (int x : arr) {
            if (x < pivot) lows.add(x);
            else if (x > pivot) highs.add(x);
            else pivots.add(x);
        }

        if (k < lows.size()) return select(lows.stream().mapToInt(i -> i).toArray(), k);
        else if (k < lows.size() + pivots.size()) return pivot;
        else return select(highs.stream().mapToInt(i -> i).toArray(), k - lows.size() - pivots.size());
    }

    public static void main(String[] args) {
        int[] arr = {7, 10, 4, 3, 20, 15};
        int k = 2;
        System.out.println("K-th smallest element is: " + select(arr, k));
    }
}