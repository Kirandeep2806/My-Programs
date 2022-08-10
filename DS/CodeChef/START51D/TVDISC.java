import java.io.*;

public class TVDISC {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            String[] s = br.readLine().split(" ");
            int a = Integer.parseInt(s[0]) - Integer.parseInt(s[2]);
            int b = Integer.parseInt(s[1]) - Integer.parseInt(s[3]);
            if(a == b)
                System.out.println("ANY");
            else if(a > b)
                System.out.println("SECOND");
            else
                System.out.println("FIRST");
        }
    }
}
