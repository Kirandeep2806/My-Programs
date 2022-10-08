import java.io.*;
import java.util.*;

public class HashSetInJava {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> hs = new HashSet<>();
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            hs.add(Integer.parseInt(inp[i]));
        Iterator<Integer> iter = hs.iterator();
        while(iter.hasNext()) {
            System.out.println(iter.next());
        }
        System.out.println(hs.size());
    }
}
