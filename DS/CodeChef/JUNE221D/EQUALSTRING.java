import java.io.*;
import java.util.*;

class EQUALSTRING {
    public static void main(String[] args)
            throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int count = 0;
            HashMap<Character, Boolean> map = new HashMap<>();
            int l = Integer.parseInt(br.readLine());
            String s1 = br.readLine();
            String s2 = br.readLine();
            for (int i = 0; i < l; i++) {
                char getS2 = s2.charAt(i);
                if ((s1.charAt(i) != getS2) && (map.getOrDefault(getS2, true))) {
                    map.put(getS2, false);
                    count++;
                }
            }
            System.out.println(count);
        }
    }
}
