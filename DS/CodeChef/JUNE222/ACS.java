import java.io.*;

public class ACS {
    public static void main(String[] args)
            throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            boolean alreadyPrinted = false;
            int n = Integer.parseInt(br.readLine());
            int solved = 0;
            while(n > 0) {
                if(solved > 9){
                    System.out.println("-1");
                    alreadyPrinted = true;
                    break;
                }
                solved++;
                if (n > 99)
                    n -= 100;
                else
                    n--;
            }
            if(!alreadyPrinted)
                System.out.println(solved);
        }
    }
}
