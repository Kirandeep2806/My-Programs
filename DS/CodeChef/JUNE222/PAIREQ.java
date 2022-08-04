import java.io.*;
import java.util.*;

public class PAIREQ {
    public static void main(String[] args) 
    throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] s = br.readLine().split(" ");
            HashMap<Integer, Integer> hm = new HashMap<>();
            int[] a = new int[n];
            int maxFreqElement = 0;
            for(int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(s[i]);
                hm.computeIfPresent(a[i], (k, v) -> v+1);
                hm.computeIfAbsent(a[i], k -> 1);
                if(hm.get(a[i]) > hm.getOrDefault(maxFreqElement, 0))
                    maxFreqElement = a[i];
            }
            System.out.println(n - hm.get(maxFreqElement));
        }
    }
}
