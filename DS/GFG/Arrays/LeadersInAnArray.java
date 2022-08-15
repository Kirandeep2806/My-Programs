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
        ArrayList<Integer> res = new ArrayList<>();
        int curLeader = arr[n-1];
        res.add(0, curLeader);
        for (int i = n-2; i >= 0; i--) {
            if(arr[i] > curLeader) {
                curLeader = arr[i];
                res.add(0, curLeader);
            }
        }
        System.out.println(res);
    }
}
