import java.util.*;

public class AssignCookies {
    public static void main(String[] args) {
        String inp;
        // int[] arr = new int[] {5,4,3,2,1};
        // Arrays.sort(arr);
        // System.out.println(Arrays.toString(arr));
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
                j++;
        }
        System.out.println(res);
        sc.close();
    }
}


// Submitted Code

// import java.util.*;

// class Solution {
//     public int findContentChildren(int[] g, int[] s) {
//         Arrays.sort(g);
//         Arrays.sort(s);
//         int i = 0, j = 0 ,res = 0, maxG=g.length, maxS=s.length;
//         while(i!=maxG && j!=maxS) {
//             if(s[j] >= g[i]) {
//                 res++;
//                 i++;
//                 j++;
//             }
//             else
//                 j++;
//         }
//         return res;
//     }
// }
