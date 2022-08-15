import java.io.*;
import java.util.*;

public class MaximumDifferenceWithoutChangeInOrder {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int ith_value = arr[0];
        int diff = Integer.MIN_VALUE;
        for (int j = 1; j < arr.length; j++) {
            if(arr[j] - ith_value > diff)
                diff = arr[j] - ith_value;
            ith_value = Math.min(ith_value, arr[j]);
        }
        System.out.println(diff);
    }
}
