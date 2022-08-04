import java.io.*;

class FLOORS {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            String[] inp = br.readLine().split(" ");
            System.out.println(Math.abs((int)Math.ceil(Float.parseFloat(inp[1])/10) - (int)Math.ceil(Float.parseFloat(inp[0])/10)));
        }
    }
}