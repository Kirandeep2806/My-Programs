import java.io.*;

public class FIT {
    public static void main(String[] args) 
    throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            System.out.println(n*10);
        }
    }
}
