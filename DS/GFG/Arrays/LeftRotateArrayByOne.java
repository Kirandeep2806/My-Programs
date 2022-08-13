import java.io.*;
import java.util.*;

public class LeftRotateArrayByOne {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int temp = arr[0];
        for (int i = 1; i < arr.length; i++)
            arr[i-1] = arr[i];
        arr[arr.length-1] = temp;
        System.out.println(Arrays.toString(arr));
    }
}
