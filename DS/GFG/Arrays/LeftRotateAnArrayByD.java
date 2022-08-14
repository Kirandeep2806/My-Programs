import java.io.*;

public class LeftRotateAnArrayByD {
    static void reverse(int[] arr, int start, int end) {
        for(int i=start, j=end; i<j; i++, j--) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
        }
    }
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int d = Integer.parseInt(br.readLine());

    }
}
