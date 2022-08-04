import java.io.*;

class MYSERVE {
    public static void main(String[] args)
    throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int a,b;
            String[] inp = br.readLine().split(" ");
            a = Integer.parseInt(inp[0]);
            b = Integer.parseInt(inp[1]);
            if((a+b)%4 == 0 || (a+b-1)%4 == 0 )
                System.out.println("Alice");
            else
                System.out.println("Bob");
        }
    }
}