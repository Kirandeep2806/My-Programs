import java.io.*;

public class LongestEvenOddSubArray {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int longestOddEvenSubArray = 1;
        int tentativeLongestOddEvenSubArray = 1;
        for (int i = 1; i < arr.length; i++) {
            if((arr[i]%2==0 && arr[i-1]%2!=0) || (arr[i]%2==1 && arr[i-1]%2==0)) {
                tentativeLongestOddEvenSubArray++;
                longestOddEvenSubArray = Math.max(longestOddEvenSubArray, tentativeLongestOddEvenSubArray);
            }
            else
                tentativeLongestOddEvenSubArray = 1;
        }
        System.out.println(longestOddEvenSubArray);
    }
}
