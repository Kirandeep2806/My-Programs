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
        int n = arr.length;
        boolean[] isNotVisited = new boolean[arr.length];
        Arrays.fill(isNotVisited, true);
        for(int i=0; i<n; i++)
            if(arr[i] <= n-1)
                isNotVisited[i] = false;
        for(int i=0; i<n; i++)
    }
}
