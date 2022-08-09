import java.io.*;

public class LuckyNumbers {
    public static boolean isLucky(int n, int... params) {
        int pos = 2;
        if(params.length != 0)
            pos = params[0];
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
        if(isLucky(n))
            System.out.println("Lucky Number");
        else
            System.out.println("Not a lucky number");
    }
}
