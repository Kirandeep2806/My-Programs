import java.io.*;

public class MaximumSubarraySum {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int n = inp.length;
        int[] arr = new int[n];
        int maxSum = Integer.MIN_VALUE;
        int sumTillNow = 0;
        for(int i=0; i<arr.length; i++) {
            arr[i] = Integer.parseInt(inp[i]);
            sumTillNow += arr[i];
            maxSum = Math.max(sumTillNow, maxSum);
            if(sumTillNow < 0)
                sumTillNow = 0;
        }
        maxSum = Math.max(sumTillNow, maxSum); // To handle the case where all the inputs are -ve
        System.out.println(maxSum);
    }
}
