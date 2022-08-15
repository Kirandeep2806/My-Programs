import java.io.*;
import java.util.*;

public class BuyAndSellStocks {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int profit = 0;
        for (int i = 1; i < arr.length; i++) {
            if(arr[i] > arr[i-1])
                profit += arr[i] - arr[i-1];
        }
        System.out.println(profit);
    }
}
