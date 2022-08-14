import java.io.*;
import java.util.Arrays;

public class LeftRotateAnArrayByD {
    static void reverse(int[] arr, int start, int end) {
        for(int i=start, j=end; i<j; i++, j--) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int n = inp.length;
        int[] arr = new int[inp.length];
        for(int i=0; i<n; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int d = Integer.parseInt(br.readLine());
        reverse(arr, 0, n-1);
        reverse(arr, n-d, n-1);
        reverse(arr, 0, n-d-1);
        System.out.println(Arrays.toString(arr));
    }
}
