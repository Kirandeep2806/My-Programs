import java.io.*;

public class NaiveSubsetSum {
    public static int subsetSumCount(int[] arr, int requiredSum, int index) {
        if(index == arr.length) {
            if(requiredSum == 0)
                return 1;
            else
                return 0;
        }
        int sum1 = subsetSumCount(arr, requiredSum, index+1);
        int sum2 = subsetSumCount(arr, requiredSum - arr[index], index+1);
        return sum1+sum2;
    }
    public static void main(String[] args)
    throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int[] arr = new int[s.length];
        for(int i=0; i<s.length; i++)
            arr[i] = Integer.parseInt(s[i]);
        int sum = Integer.parseInt(br.readLine());
        System.out.println(subsetSumCount(arr, sum, 0));
    }
}
