import java.io.*;

class FindUniqueMultiplicationPairs {
    public static void main(String[] args) 
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()), i=1;
        while(i <= Math.sqrt(n)) {
            if(n%i == 0)
                System.out.printf("%d * %d\n", i, n/i);
            i++;
        }
    }
}