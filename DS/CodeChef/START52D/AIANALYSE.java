import java.io.*;
import java.util.*;

public class AIANALYSE {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(Integer.parseInt(br.readLine()) > 1000 ? "No" : "Yes");
    }
}
