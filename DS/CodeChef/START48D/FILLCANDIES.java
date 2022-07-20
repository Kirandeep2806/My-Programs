import java.io.*;
import java.util.Arrays;

public class FILLCANDIES {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-- > 0) {
            double[] arr = Arrays.stream(br.readLine().split(" ")).mapToDouble(Double::parseDouble).toArray();
            System.out.println((int)Math.ceil(arr[0]/(arr[1]*arr[2])));
        }
    }
}
