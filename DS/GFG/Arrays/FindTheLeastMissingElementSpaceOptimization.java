import java.io.*;
import java.util.*;

public class FindTheLeastMissingElementSpaceOptimization {
    public static int[] swap(int[] arr, int pos) {
        arr[pos] = arr[pos]^arr[arr[pos]];
        arr[arr[pos]] = arr[pos]^arr[arr[pos]];
        arr[pos] = arr[pos]^arr[arr[pos]];
        return arr;
    }

    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int n = arr.length, i = 0;
        for(;i<n;i++) {
            if(arr[i]!=i && arr[i]<n)
                swap(arr, i);
        }
        
    }
}
