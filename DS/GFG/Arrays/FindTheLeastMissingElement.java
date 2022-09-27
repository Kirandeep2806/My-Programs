import java.io.*;
import java.util.*;

public class FindTheLeastMissingElement {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int n = arr.length, i = 0;
        boolean[] isNotVisited = new boolean[arr.length];
        Arrays.fill(isNotVisited, true);
        for(;i<n;i++)
            if(arr[i] <= n-1)
                isNotVisited[arr[i]] = false;
        i=0;
        for(;i<n;i++)
            if(isNotVisited[i])
                break;
        System.out.println(i);
    }
}
