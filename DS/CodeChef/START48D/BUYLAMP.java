import java.io.*;
import java.util.Arrays;

public class BUYLAMP {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int res = 0;
            res += arr[1]*arr[2];
            arr[0] -= arr[1];
            res += Math.min(arr[2], arr[3])*arr[0];
            System.out.println(res);
        }
    }
}
