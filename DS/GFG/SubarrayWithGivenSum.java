/**
 * SubarrayWithGivenSum
 */

    // { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class SubarrayWithGivenSum{
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // int t = sc.nextInt();

        // for (int i = 0; i < t; i++) {

            String[] sInput = sc.nextLine().split(" ");
            int n = Integer.parseInt(sInput[0]);
            int s = Integer.parseInt(sInput[1]);

            int[] m = new int[n];
            sInput = sc.nextLine().split(" ");
            for (int j = 0; j < sInput.length; j++) {
                m[j] = Integer.parseInt(sInput[j]);
            }
            
            Solution obj = new Solution();
            ArrayList<Integer> res = obj.subarraySum(m, n, s);
            for(int ii = 0;ii<res.size();ii++)
                System.out.print(res.get(ii) + " ");
            System.out.println();
        // }
    }

}// } Driver Code Ends


class Solution
{
    //Function to find a continuous sub-array which adds up to a given number.
    static ArrayList<Integer> subarraySum(int[] arr, int n, int s) 
    {
        ArrayList<Integer> l = new ArrayList<>();
        int sum = 0, start=0, i=0;
        Boolean flag = true;
        while(i < n) {
            if(flag) {
                sum += arr[i];
                i++;
            }
            // System.out.println(sum);
            if(sum > s) {
                sum -= arr[start];
                start++;
                flag = false;
            }
            else
                flag = true;
            if(sum == s) {
                l.add(start+1);
                l.add(i);
                break;
            }
        }
        if(l.isEmpty())
            l.add(-1);
        return l;
    }
}
