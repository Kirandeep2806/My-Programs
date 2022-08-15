import java.io.*;
import java.util.*;

public class TrappingRainWater {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int n = arr.length, waterTrapped=0;
        int[] leftMaxArr = new int[n];
        int[] rightMaxArr = new int[n];
        leftMaxArr[0] = arr[0];
        rightMaxArr[n-1] = arr[n-1];
        for(int i=1; i<n; i++)
            leftMaxArr[i] = Math.max(arr[i], leftMaxArr[i-1]);
        for(int i=n-2; i>=0; i--)
            rightMaxArr[i] = Math.max(arr[i], rightMaxArr[i+1]);
        for(int i=1; i<n-1; i++)
            waterTrapped += Math.min(leftMaxArr[i], rightMaxArr[i]) - arr[i];
        System.out.println(waterTrapped);
    }
}
