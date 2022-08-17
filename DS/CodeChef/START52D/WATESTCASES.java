import java.io.*;
import java.util.*;

public class WATESTCASES {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] inp = br.readLine().split(" ");
            int[] sizes = new int[inp.length];
            for(int i=0; i<sizes.length; i++)
                sizes[i] = Integer.parseInt(inp[i]);
            char[] bArr = br.readLine().toCharArray();
            int getMin = Integer.MAX_VALUE;
            for(int i=0; i<n; i++) {
                if(bArr[i] == '0')
                    getMin = Math.min(getMin, sizes[i]);
            }
            System.out.println(getMin);
        }
    }
}
