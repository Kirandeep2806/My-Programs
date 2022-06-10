import java.io.*;

public class ALTERADD {
    public static void main(String[] args) 
    throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            String[] inp = br.readLine().split(" ");
            int a = Integer.parseInt(inp[0]);
            int b = Integer.parseInt(inp[1]);
            if((b-a+1)%3 == 0)
                System.out.println("NO");
            else
                System.out.println("YES");
        }
    }
}
