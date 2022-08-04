import java.io.*;

// BruteForce

// Time - O(n^2)
// Space - O(1)

class Solution1 {
    public int maxProfit(int[] prices) {
        int max = 0;
        for(int buy=0; buy<prices.length; buy++) {
            for(int sell=buy; sell<prices.length; sell++) {
                if((prices[sell]-prices[buy]) > max)
                    max = prices[sell]-prices[buy];
            }
        }
        return max;
    }
}

// Optimal

class Solution2 {
    public int maxProfit(int[] prices) {
        int minSoFar = Integer.MAX_VALUE;
        int maxProfit = 0;
        for(int i=0; i<prices.length; i++) {
            if(prices[i] < minSoFar)
                minSoFar = prices[i];
            if((prices[i] - minSoFar) > maxProfit)
                maxProfit = prices[i] - minSoFar;
        }
        System.out.printf("Min So Far %d, Max Profit %d\n", minSoFar, maxProfit);
        return maxProfit;
    }
}

public class BestTimeToBuyAndSellStock {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split(" ");
        int[] n = new int[arr.length];
        for(int i=0; i<arr.length; i++)
            n[i] = Integer.parseInt(arr[i]);
        // System.out.println(Arrays.toString(n));
        // System.out.println(new Solution1().maxProfit(n));
        System.out.println(new Solution2().maxProfit(n));
    }
}
