import java.io.*;
import java.util.Arrays;

public class MoveAllZeroesToEnd {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int nonZeroCount = 0;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] != 0) {
                int temp = arr[i];
                arr[i] = arr[nonZeroCount];
                arr[nonZeroCount] = temp;
                nonZeroCount++;
            }
        }
        System.out.println(Arrays.toString(arr));
    }
}
