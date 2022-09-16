// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

public class DigitsInPower {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int x = Integer.parseInt(inputLine[0]);
            int n = Integer.parseInt(inputLine[1]);
            int[] ans = new Solve().getFreq(x, n);
            for (int sec : ans) {
                System.out.print(sec + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


//User function Template for Java


class Solve {
    int[] getFreq(int x, int n) {
        // System.out.println((long)Math.pow(x, n));
        // System.out.println((int)Math.pow(x, n));
        int[] arr = new int[10];
        Arrays.fill(arr, 0);
        for(int i=1; i<=n; i++) {
            long temp = (long)Math.pow(x, i);
            System.out.println(temp);
            while(temp!=0) {
                arr[(int)(temp%10)] += 1;
                temp /= 10;
            }
        }
        return arr;
    }
}
