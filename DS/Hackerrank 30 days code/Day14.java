import java.util.*;

class Difference {
    private int[] elements;
    public int maximumDifference = Integer.MIN_VALUE;

    Difference(int[] a) {
        this.elements = a;
    }

    public void computeDifference() {
        int temp = 0;
        for (int i = 0; i < this.elements.length - 1; i++) {
            for (int j = i + 1; j < this.elements.length; j++) {
                temp = Math.abs(this.elements[i] - this.elements[j]);
                if (temp > maximumDifference)
                    maximumDifference = temp;
            }
        }
    }

}

public class Day14 { // public class Solution

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();

        Difference difference = new Difference(a);

        difference.computeDifference();

        System.out.print(difference.maximumDifference);
    }
}