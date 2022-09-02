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
        int kadanesMaxSum = MaximumSubArray(arr);
        System.out.println("Kadane's sum : " + kadanesMaxSum);
        if(kadanesMaxSum < 0)
            System.out.println(kadanesMaxSum);
        else {
            int arraySum = 0;
            for (int i = 0; i < arr.length; i++) {
                arraySum += arr[i];
                arr[i] = -arr[i];
            }
            int circularMaxSum = arraySum + MaximumSubArray(arr);
            System.out.println("Circular sum : " + circularMaxSum);
            int finalResult = Math.max(circularMaxSum, kadanesMaxSum);

            System.out.println(finalResult);
        }
    }
}
