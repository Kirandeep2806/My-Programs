import java.io.*;

public class DIFFMED {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int i, j;
            for(i=1, j=n; i<=n/2; i++, j--)
                System.out.printf("%d %d ", j, i);
            if(n%2 == 1)
                System.out.println(n/2+1);
            else
                System.out.println();
        }
    }
}
