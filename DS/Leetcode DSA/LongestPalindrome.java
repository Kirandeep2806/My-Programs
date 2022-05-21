import java.util.*;

class LongestPalindrome {
    public static void main(String[] args) {
        String s;
        int length=0;
        boolean maxOddValue=false;
        Scanner in = new Scanner(System.in);
        s = in.next();
        HashMap<Character, Integer> hm = new HashMap<>();
        for(char i: s.toCharArray()) {
            if(hm.containsKey(i))
                hm.put(i, hm.get(i) + 1);
            else
                hm.put(i, 1);
        }

        System.out.println(hm.toString());

        for (Map.Entry<Character, Integer> m: hm.entrySet()) {
            if(m.getValue()%2 == 0)
                length += m.getValue();
            else {
                length += m.getValue() - 1;
                maxOddValue = true;
            }
        }
        if(maxOddValue)
            length++;
        System.out.println(length);
        in.close();
    }
}