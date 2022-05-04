import java.util.*;

public class HashMapsJava {
    public static void main(String[] args) {
        HashMap<Integer, String> map = new HashMap<>();
        map.put(1, "Kiran");
        map.put(2, "Raj");
        map.put(3, "Rajesh");
        for (Map.Entry<Integer, String> m : map.entrySet()) {
            System.out.println(m.getKey() + " " + m.getValue());
        }
    }
}
