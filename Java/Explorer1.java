import java.util.*;
import java.util.stream.IntStream;
public class Explorer1 {
    public static void main(String[] args) {
        int[] arr = {1,2,3,5,-3,4};
        Integer[] boxedInts = IntStream.of(arr).boxed().toArray(Integer[]::new);
        System.out.println(boxedInts.getClass());
        System.out.println("Hi");
        Arrays.parallelSort(arr);
        // ArrayList<Integer> al = new ArrayList<>(Arrays.asList(arr));
        // Collections.reverse();
        // Arrays.fill(arr, 0);
        System.out.println(Arrays.toString(arr));
    }
}
