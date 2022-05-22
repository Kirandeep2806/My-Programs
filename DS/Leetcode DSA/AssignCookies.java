import java.util.*;

public class AssignCookies {
    public static void main(String[] args) {
        String inp;
        ArrayList<Integer> g = new ArrayList<>();
        ArrayList<Integer> s = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        inp = sc.nextLine();
        for (String i : inp.split(" "))
            g.add(Integer.parseInt(i));
        inp = sc.nextLine();
        for (String i : inp.split(" "))
            s.add(Integer.parseInt(i));
        // System.out.println(g + " " + s);
        g.sort((a, b) -> a.compareTo(b));
        s.sort((a, b) -> a.compareTo(b));
        // System.out.println(g + " " + s);
        int i = 0, j = 0 ,res = 0, maxG=g.size(), maxS=s.size();
        while(i!=maxG && j!=maxS) {
            if(s.get(j) >= g.get(i)) {
                res++;
                i++;
                j++;
            }
            else
                break;
        }
        System.out.println(res);
        sc.close();
    }
}
