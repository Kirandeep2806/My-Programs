import java.io.*;
import java.util.*;

public class LeadersInAnArray {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int n = inp.length;
        int[] arr = new int[n];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int currLeader = arr[n-1];
        for (int i = n-2; i >= 0; i++) {
            if(arr[i] > currLeader) {
            }
        }
    }
}
