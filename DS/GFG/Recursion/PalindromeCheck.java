import java.io.*;

class PalindromeCheck {
    public static boolean checkPalindrome(String s, int start, int end) {
        if(start >= end)
            return true;
        if(s.charAt(start) == s.charAt(end))
            return checkPalindrome(s, start+1, end-1);
        else
            return false;
    }
    public static void main(String[] args)
    throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        System.out.println(checkPalindrome(s, 0, s.length()-1));
    }
}
