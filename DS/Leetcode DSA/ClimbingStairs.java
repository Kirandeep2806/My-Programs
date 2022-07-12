import java.io.*;
import java.util.Arrays;

class Solution {
    public int climbStairs(int n, int... dp) {
        // System.out.println(dp.length);
        // if(dp.length > 0) {
        if(dp.length == 0) {
            dp = new int[n+1];
            Arrays.fill(dp, -1);
        }
        if(n == 0)
            return 1;
        if(n < 0)
            return 0;
        if(dp[n] != -1)
            return dp[n];
        dp[n] = climbStairs(n-1, dp) + climbStairs(n-2, dp);
        return dp[n];
    }
}

class ClimbingStairs {
    public static void main(String[] args)
    throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Solution solution = new Solution();
        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        System.out.println(solution.climbStairs(n));
    }
}
