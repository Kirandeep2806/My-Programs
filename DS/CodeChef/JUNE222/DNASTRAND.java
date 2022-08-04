import java.io.*;
import java.util.*;

public class DNASTRAND {
    public static void main(String[] args)
            throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        HashMap<Character, Character> hm = new HashMap<>();
        hm.put('A', 'T');
        hm.put('T', 'A');
        hm.put('C', 'G');
        hm.put('G', 'C');
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String s = br.readLine();
            StringBuffer f = new StringBuffer();
            while (n-- > 0)
                f.insert(0, hm.get(s.charAt(n)));
            System.out.println(f.toString());
            // System.out.println(f);
        }
    }
}
