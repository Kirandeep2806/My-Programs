import java.io.*;

class Solution {
    public int climbStairs(int n) {
        if(n == 0)
            return 1;
        if(n < 0)
            return 0;
        return climbStairs(n-1) + climbStairs(n-2);
    }
}

class ClimbingStairs {
    public static void main(String[] args)
    throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Solution solution = new Solution();
        System.out.println(solution.climbStairs(n));
    }
}
