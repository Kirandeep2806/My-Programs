import java.io.*;
import java.util.*;

public class MaximumConsecutive1sInBinaryArray {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        int max_1s = Integer.MIN_VALUE;
        int tempCounterFor1 = 0;
        for(int i=0; i<arr.length; i++) {
            arr[i] = Integer.parseInt(inp[i]);
            if(arr[i] == 1)
                tempCounterFor1++;
            if(arr[i] == 0) {
                max_1s = Integer.max(max_1s, tempCounterFor1);
                tempCounterFor1 = 0;
            }
        }
        max_1s = Integer.max(max_1s, tempCounterFor1);
        System.out.println(max_1s);
    }
}
