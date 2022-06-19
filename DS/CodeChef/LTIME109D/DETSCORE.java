import java.io.*;

class DETSCORE {
    public static void main(String[] args)
    throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int x,n;
            String[] inp = br.readLine().split(" ");
            x = Integer.parseInt(inp[0]);
            n = Integer.parseInt(inp[1]);
            System.out.println(x/10*n);
        }
    }
}
