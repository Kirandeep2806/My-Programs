
/**
 * sieveOfEratosthenes
 */

import java.util.*;

public class sieveOfEratosthenes {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the upto where you want to print primes : ");
        int n = sc.nextInt();
        boolean[] primes = new boolean[n + 1];
        Arrays.fill(primes, true);
        primes[0] = primes[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (primes[i]) {
                for (int j = 2 * i; j <= n; j += i) {
                    primes[j] = false;
                }
            }
        }
        int count = 0;
        for (boolean i : primes) {
            if (i)
                System.out.print(count + " ");
            count++;
        }
        sc.close();
    }
}