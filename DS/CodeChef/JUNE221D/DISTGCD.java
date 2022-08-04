import java.io.*;
class DISTGCD {
    public static void main(String[] args) 
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            String[] inp = br.readLine().split(" ");
            int a = Integer.parseInt(inp[0]);
            int b = Integer.parseInt(inp[1]);
            int diff = Math.abs(a - b);
            int count = 0;
            int temp = 1;
            while(temp <= diff/2) {
                if(diff%temp == 0)
                    count++;
                temp++;
            }
            count++;
            System.out.println(count);
        }
    }
}
