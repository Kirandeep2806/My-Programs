import java.util.*;

class LongestPalindrome {
    public static void main(String[] args) {
        String s;
        Scanner in = new Scanner(System.in);
        s = in.next();
        HashMap<Character, Integer> hm = new HashMap<>();
        for(char i: s.toCharArray()) {
            if(hm.containsKey(i))
                hm.put(i, hm.get(i) + 1);
            else
                hm.put(i, 1);
        }

        for (Map.Entry<Character, Integer> m: hm.entrySet()) {
            System.out.println(m.getKey() + " " + m.getValue());
        }
        in.close();
    }
}