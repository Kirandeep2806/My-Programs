import java.util.*;
import java.io.*;

public class HashMapsJava{
    public static void main(String[] args)
    throws IOException {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "Kiran");
        map.put(2, "Raj");
        map.put(3, "Rajesh");
        System.out.printf("%s\n%s\n%s\n", map.entrySet(), map.keySet(), map.values());
        map.remove(1);
        map.computeIfAbsent(4, k -> "Default"); // Set to default if key not present
        map.computeIfPresent(4, (k, v) -> v + " Kiran"); // Update the value if it present
        System.out.printf("After removing key 1 : %s\n", map.entrySet());
        for (Map.Entry<Integer, String> m : map.entrySet()) {
            System.out.println(m.getKey() + " " + m.getValue());
        }
        System.out.println();

        // Compute the frequency of numbers in an array.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
            int[] intInput = new int[inp.length];
            for(int i=0; i<inp.length; i++)
                intInput[i] = Integer.parseInt(inp[i]);
        HashMap<Integer, Integer> hm = new HashMap<>();
        for(int i=0; i<intInput.length; i++)
            hm.compute(intInput[i], (k, v) -> v==null?1:++v);
    }
}
