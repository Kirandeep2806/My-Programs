import java.util.*;

public class HashMapsJava {
    public static void main(String[] args) {
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
    }
}
