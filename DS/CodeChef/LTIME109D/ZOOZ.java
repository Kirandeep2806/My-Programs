import java.io.*;

public class ZOOZ {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n;
            n = Integer.parseInt(br.readLine());
            if((n & 1) == 1) {
                System.out.print("0");
                for(int i = 0; i < n/2; i++)
                    System.out.print("10");
            }
            else {
                if(((n/2)&1) == 1) {
                    for(int i = 0; i < n/2; i++){
                        if(i < n/4)
                            System.out.print("10");
                        else if(i == n/4)
                            System.out.print("11");
                        else
                            System.out.print("01");
                    }
                }
                else {
                    for(int i = 0; i < n/2; i++){
                        if(i < n/4)
                            System.out.print("10");
                        else
                            System.out.print("01");
                    }
                }
            }
            System.out.println();
        }
    }
}
