import java.io.*;
import java.util.Arrays;

public class GRIDBL {
    public static void main(String[] args)
            throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            // --------------Not working --------
            
            // int res = 0;
            // if ((arr[0] == 1) || (arr[1] == 1)) {
            //     if((arr[0]+arr[1])%2 == 0)
            //         System.out.println(1);
            //     else
            //         System.out.println(0);
            // }
            // else {
            //     if ((arr[0] % 2 == 0) && (arr[1] % 2 != 0))
            //         System.out.println(arr[0]);
            //     else if ((arr[0] % 2 != 0) && (arr[1] % 2 == 0))
            //         System.out.println(arr[1]);
            //     else if ((arr[0] % 2 != 0) && (arr[1] % 2 != 0))
            //         System.out.println(arr[0] + arr[1]);
            //     else
            //         System.out.println(0);
            // }

            // --------------Working --------

            int n = arr[0]>>1<<1;
            int m = arr[1]>>1<<1;
            System.out.println((arr[0]*arr[1])-(n*m));
        }
    }
}
