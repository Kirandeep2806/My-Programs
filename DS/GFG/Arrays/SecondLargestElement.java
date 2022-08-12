import java.io.*;

public class SecondLargestElement {
    public static void main(String[] args)
    throws java.lang.Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inp = br.readLine().split(" ");
        int[] arr = new int[inp.length];
        for(int i=0; i<inp.length; i++)
            arr[i] = Integer.parseInt(inp[i]);
        int largest=0, res=-1;
        for (int i = 1; i < arr.length; i++) {
            if(arr[i] > arr[largest]) {
                res = largest;
                largest = i;
            }
            else if(arr[i] < arr[largest]) {
                // if(res == -1)
                //     res = i;
                // if(arr[res] < arr[i])
                //     res = i;
                // Instead we write with OR.
                if(res == -1 || arr[res] < arr[i])
                    res = i;
            }
        }
        System.out.println("Second largest element : " + arr[res]);
    }
}
