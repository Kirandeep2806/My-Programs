import java.io.*;
import java.util.Arrays;

public class FAIRPASS {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            System.out.println(arr[0]+1 <= arr[1] ? "YES" : "NO");
        }
    }
}
