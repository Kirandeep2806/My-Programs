import java.io.*;

class DIVBYI {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int mid = (int)Math.ceil(((float)n)/2), midNext = mid + 1;
            if((n&1) == 1) {
                System.out.print(mid + " ");
                mid--;
            }
            for(int i=0; i<n/2; i++, mid--, midNext++)
                System.out.print(mid + " " + midNext + " ");
            System.out.println();
        }
    }
}