import java.io.*;

public class SPLITN {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int countOfOnes = -1;
            while(n > 0) {
                n = n&(n-1);
                countOfOnes++;
            }
            System.out.println(countOfOnes);
        }
    }
}
