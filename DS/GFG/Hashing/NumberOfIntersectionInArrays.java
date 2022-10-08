import java.io.*;
import java.util.*;

public class NumberOfIntersectionInArrays {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        HashSet<Integer> hs1 = new HashSet<>();
        HashSet<Integer> hs2 = new HashSet<>();
        for(int i=0; i<inp.length; i++)
            hs1.add(Integer.parseInt(inp[i]));
        inp = br.readLine().split(" ");
        for(int i=0; i<inp.length; i++)
        hs2.add(Integer.parseInt(inp[i]));
        int res = 0;
        Iterator<Integer> iter = hs2.iterator();
        while(iter.hasNext()) {
            int curVal = iter.next();
            if(hs1.contains(curVal)) {
                res++;
                hs1.remove(curVal);
            }
        }
        System.out.println(res);
    }
}
