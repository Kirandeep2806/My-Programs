import java.io.*;
public class SUBSCRIBE_ {
    public static void main(String[] args) 
    throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String[] inp = br.readLine().split(" "); 
            int n = Integer.parseInt(inp[0]);
            int x = Integer.parseInt(inp[1]);
            System.out.println((int)Math.ceil(((float)n)/6)*x);
        }
    }
}
