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
        System.out.println(g + " " + s);
        g.sort((a, b) -> a.compareTo(b));
        s.sort((a, b) -> a.compareTo(b));
        System.out.println(g + " " + s);
        sc.close();
    }
}
