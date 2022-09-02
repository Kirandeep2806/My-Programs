import java.io.*;
import java.util.*;

public class MaximumCircularSubArray {

    public static int MaximumSubArray(int... arr) {
        int maxSum = Integer.MIN_VALUE;
        int tempSum = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if(tempSum < 0)
                tempSum = 0;
            tempSum += arr[i];
            maxSum = Math.max(tempSum, maxSum);
        }
        return maxSum;
    }

    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int res = MaximumSubArray(arr);
        System.out.println(res);
    }
}
