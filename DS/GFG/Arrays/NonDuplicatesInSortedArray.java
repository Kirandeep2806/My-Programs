import java.io.*;

public class NonDuplicatesInSortedArray {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++) 
            arr[i] = Integer.parseInt(inp[i]);
        int res = 0;
        System.out.print(arr[res] + " ");
        for (int i = 1; i < arr.length; i++) {
            if(arr[res] != arr[i]) {
                System.out.print(arr[i] + " ");
                res = i;
            }
        }
    }
}
