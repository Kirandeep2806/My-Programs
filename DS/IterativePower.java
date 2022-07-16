import java.io.*;

public class IterativePower
{
	public static void main(String[] args)
	throws IOException{
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    int base = Integer.parseInt(br.readLine());
	    int exponent = Integer.parseInt(br.readLine());
	    int result = 1;
	    int exponentClone = exponent;
	    int baseClone = base;
	    if(exponent >= 0) {
    	    while(exponentClone != 0) {
    	        if((exponentClone&1) == 1)
    	            result *= baseClone;
    	        baseClone *= baseClone;
    	        exponentClone >>= 1;
    	    }
    		System.out.println(result);
	    }
	}
}
