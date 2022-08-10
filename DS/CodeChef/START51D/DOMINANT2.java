import java.io.*;
import java.util.*;

public class DOMINANT2 {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] inp = br.readLine().split(" ");
            int[] intInput = new int[n];
            for(int i=0; i<n; i++)
                intInput[i] = Integer.parseInt(inp[i]);
            HashMap<Integer, Integer> hm = new HashMap<>();
            for(int i=0; i<n; i++)
                hm.compute(intInput[i], (k, v) -> v==null?1:++v);
            boolean isAnythingSame = false;
            int maxCount = 0;
            for(Map.Entry<Integer, Integer> m: hm.entrySet()) {
                if(m.getValue() == maxCount)
                    isAnythingSame = true;
                if(m.getValue() > maxCount) {
                    maxCount = m.getValue();
                    isAnythingSame = false;
                }
            }
            if(isAnythingSame)
                System.out.println("NO");
            else
                System.out.println("YES");
        }
    }
}
