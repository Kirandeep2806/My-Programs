import java.io.*;
import java.util.*;

public class SubarrayWithSumZero {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);

        HashSet<Integer> hs = new HashSet<>();
        int prefixSum = 0, i = 0;
        for (;i < arr.length; i++) {
            prefixSum += arr[i];
            if(prefixSum == 0) // Handle corner case - (-3 2 1 4)
                break;
            if(hs.contains(prefixSum))
                break;
            else
                hs.add(prefixSum);
        }
        if(i == arr.length)
            System.out.println("No");
        else
            System.out.println("Yes");
    }
}
