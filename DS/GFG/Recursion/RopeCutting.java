import java.io.*;

public class RopeCutting {

    public static int maxRopes(int n, int a, int b, int c, int ropeCount) {
        if(n == 0)
            return ropeCount;
        else if(n < 0)
            return -1;
        int maxFromFirst = maxRopes(n-a, a, b, c, ropeCount+1);
        int maxFromSecond = maxRopes(n-b, a, b, c, ropeCount+1);
        int maxFromThird = maxRopes(n-c, a, b, c, ropeCount+1);
        return Math.max(Math.max(maxFromFirst, maxFromSecond), maxFromThird);
    }
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int[] arr = new int[s.length];
        for(int i=0; i<s.length; i++)
            arr[i] = Integer.parseInt(s[i]);
        System.out.println(maxRopes(arr[0], arr[1], arr[2], arr[3], 0));
    }
}
