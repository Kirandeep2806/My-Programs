import java.io.*;

public class FindTheLeastMissingElementSpaceOptimization {
    public static int[] swap(int[] arr, int pos) {
        int temp1=arr[pos], temp2=arr[arr[pos]];
        arr[pos] = temp2;
        arr[temp1] = temp1;
        return arr;
    }

    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<arr.length; i++)
            arr[i] = Integer.parseInt(inp[i]);

        // Code Begins

        int n = arr.length, i = 0;
        for(;i<n;i++) {
            if(arr[i]!=i && arr[i]<n)
                swap(arr, i);
        }
        i=0;
        for(;i<n;i++)
            if(arr[i]!=i)
                break;
        System.out.println(i);
    }
}
