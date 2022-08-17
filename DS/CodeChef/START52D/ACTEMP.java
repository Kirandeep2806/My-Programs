import java.io.*;
import java.util.*;

public class ACTEMP {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            String[] inp = br.readLine().split(" ");
            int[] arr = new int[inp.length];
            int getMax = 1;
            for(int i=0; i<arr.length; i++) {
                arr[i] = Integer.parseInt(inp[i]);
                getMax = Math.max(getMax, arr[i]);
            }
            System.out.println(arr[1] == getMax ? "Yes" : "No");
        }
    }
}
