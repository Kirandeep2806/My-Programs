import java.io.*;

public class LuckyNumbers {
    public static boolean isLucky(int n, int pos) {
        if(pos > n)
            return true;
        if(n%pos == 0)
            return false;
        return isLucky(n-n/pos, pos+1);
    }

    public static void main(String[] args)
    throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if(isLucky(n, 2))
            System.out.println("Lucky Number");
        else
            System.out.println("Not a lucky number");
    }
}
