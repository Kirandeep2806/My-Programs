import java.io.*;

public class SubsetGeneration {
    public static void main(String[] args)
    throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        generateSubsets(s, "", 0);
    }
    
    public static void generateSubsets(String s, String res, int index) {
        if(index == s.length()) {
            System.out.println(res);
            return;
        }
        generateSubsets(s, res, index+1);
        generateSubsets(s, res + s.charAt(index), index+1);
    }
}
